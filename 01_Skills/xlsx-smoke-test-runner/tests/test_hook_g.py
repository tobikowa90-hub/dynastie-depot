"""TDD-Tests für Hook-§G Sparrate-Σ-Sanity (SPEC §4.3) + P13 sheets-Expand."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import openpyxl
import pytest
import yaml

_HOOK = Path(__file__).resolve().parents[3] / "03_Tools" / "precommit" / "xlsx_smoke_test.py"


def _load_hook():
    spec = importlib.util.spec_from_file_location("hook_under_test", _HOOK)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["hook_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


# ----- _derive_rate_eur unit-tests (SPEC §4.3 Akzeptanz #1-4) -----


def test_derive_rate_eur_flag_true_returns_zero():
    mod = _load_hook()
    assert mod._derive_rate_eur({"flag": True, "defcon": 3}) == 0
    assert mod._derive_rate_eur({"flag": True, "defcon": 2}) == 0


def test_derive_rate_eur_flag_false_d3_d4_returns_38():
    mod = _load_hook()
    assert mod._derive_rate_eur({"flag": False, "defcon": 3}) == 38
    assert mod._derive_rate_eur({"flag": False, "defcon": 4}) == 38


def test_derive_rate_eur_flag_false_d2_returns_19():
    mod = _load_hook()
    assert mod._derive_rate_eur({"flag": False, "defcon": 2}) == 19


def test_derive_rate_eur_flag_false_d1_returns_zero():
    mod = _load_hook()
    assert mod._derive_rate_eur({"flag": False, "defcon": 1}) == 0


def test_derive_rate_eur_unmapped_defcon_raises():
    mod = _load_hook()
    with pytest.raises(ValueError):
        mod._derive_rate_eur({"flag": False, "defcon": 5})


# ----- _check_g_sparrate_sigma -----


def _build_sat_wb_clean() -> openpyxl.Workbook:
    """Minimaler Sat-konformer Workbook: 2 Sheets + N19-Sanity + K3-Display."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Satelliten Monitor"
    ws["K3"] = "Ergebnis: ● 7 Voll  ● 1 D2-Sockelbetrag (V)  ● 4 Eingefroren"
    ws["N19"] = "→ muss = 285,00 €"
    wb.create_sheet("QuickScreen Ampel")
    return wb


def _build_sat_wb_bad_display() -> openpyxl.Workbook:
    wb = _build_sat_wb_clean()
    wb["Satelliten Monitor"]["N19"] = "→ muss = 999,00 €"
    return wb


def _write_config_yaml(tmp_path: Path, satelliten: list[dict], anker: int = 285) -> Path:
    p = tmp_path / "config.yaml"
    cfg = {
        "brokers": {"scalable": {"sparrate_eur": anker}},
        "satelliten": satelliten,
    }
    p.write_text(yaml.safe_dump(cfg, allow_unicode=True), encoding="utf-8")
    return p


def _live_config_yaml_path() -> Path:
    return _HOOK.resolve().parents[2] / "01_Skills" / "dynastie-depot" / "config.yaml"


def _build_canonical_sat_list_285() -> list[dict]:
    """7×D3 + 1×D2 (V noFLAG) + 4×FLAG = 285 (empirie drift-doc §2.4)."""
    return [
        {"ticker": "ASML", "defcon": 3, "flag": False},
        {"ticker": "AVGO", "defcon": 2, "flag": True},
        {"ticker": "MSFT", "defcon": 2, "flag": True},
        {"ticker": "COST", "defcon": 3, "flag": False},
        {"ticker": "RMS", "defcon": 3, "flag": False},
        {"ticker": "VEEV", "defcon": 3, "flag": False},
        {"ticker": "SU", "defcon": 3, "flag": False},
        {"ticker": "BRK.B", "defcon": 3, "flag": False},
        {"ticker": "V", "defcon": 2, "flag": False},
        {"ticker": "TMO", "defcon": 3, "flag": False},
        {"ticker": "APH", "defcon": 2, "flag": True},
        {"ticker": "AMZN", "defcon": 1, "flag": True},
    ]


def test_check_g_passes_on_canonical_sat_and_config(tmp_path):
    mod = _load_hook()
    cfg = _write_config_yaml(tmp_path, _build_canonical_sat_list_285())
    wb = _build_sat_wb_clean()
    err = mod._check_g_sparrate_sigma(wb, cfg)
    assert err is None, f"§G fail unexpected: {err}"


def test_check_g_fails_when_sigma_mismatches_anker(tmp_path):
    mod = _load_hook()
    sats = _build_canonical_sat_list_285()
    sats[10]["flag"] = False  # APH D2 noFLAG → Σ +19 = 304 ≠ 285
    cfg = _write_config_yaml(tmp_path, sats)
    wb = _build_sat_wb_clean()
    err = mod._check_g_sparrate_sigma(wb, cfg)
    assert err is not None
    assert "Σ" in err or "Sigma" in err or "285" in err


def test_check_g_n19_expected_text_derives_from_anker(tmp_path):
    """Codex-R3 MED-2: N19 expected-string aus anker abgeleitet, NICHT hardcoded 285.

    Mit anker=380 (alternative Sparrate) + Display N19='→ muss = 380,00 €' → PASS.
    """
    mod = _load_hook()
    # 10×D3 = 380€
    sats = [{"ticker": f"X{i}", "defcon": 3, "flag": False} for i in range(10)]
    cfg = _write_config_yaml(tmp_path, sats, anker=380)
    wb = _build_sat_wb_clean()
    wb["Satelliten Monitor"]["N19"] = "→ muss = 380,00 €"
    err = mod._check_g_sparrate_sigma(wb, cfg)
    assert err is None, f"§G fail bei alternative anker: {err}"


def test_check_g_n19_fails_when_text_mismatches_derived_anker(tmp_path):
    """Codex-R3 MED-2: bei anker=380 muss N19='285,00' FAIL (Display-Drift)."""
    mod = _load_hook()
    sats = [{"ticker": f"X{i}", "defcon": 3, "flag": False} for i in range(10)]
    cfg = _write_config_yaml(tmp_path, sats, anker=380)
    wb = _build_sat_wb_clean()  # N19 still says '→ muss = 285,00 €'
    err = mod._check_g_sparrate_sigma(wb, cfg)
    assert err is not None
    assert "N19" in err
    assert "380" in err  # derived from anker, not hardcoded 285


def test_check_g_fails_on_n19_display_drift(tmp_path):
    mod = _load_hook()
    cfg = _write_config_yaml(tmp_path, _build_canonical_sat_list_285())
    wb = _build_sat_wb_bad_display()
    err = mod._check_g_sparrate_sigma(wb, cfg)
    assert err is not None
    assert "N19" in err


@pytest.mark.integration
def test_check_g_passes_on_live_config_yaml_and_canonical_wb():
    """Codex-R3 LOW-1: Integrationstest — Live config.yaml + canonical Sat-Workbook → PASS."""
    mod = _load_hook()
    cfg_path = _live_config_yaml_path()
    if not cfg_path.is_file():
        pytest.skip(f"Live config.yaml fehlt: {cfg_path}")
    wb = _build_sat_wb_clean()
    err = mod._check_g_sparrate_sigma(wb, cfg_path)
    assert err is None, f"§G fail gegen Live-config: {err}"


# ----- P13 Sheets-Tupel-Expansion -----


def test_p13_rebal_profile_includes_us_exposure_and_parameter():
    mod = _load_hook()
    sheets = mod._PROFILES["Rebalancing_Tool"]["sheets"]
    assert "Portfolio & Rebalancing" in sheets
    assert "US-Exposure" in sheets
    assert "Parameter & Regeln" in sheets


def test_p13_sat_profile_includes_quickscreen_ampel():
    mod = _load_hook()
    sheets = mod._PROFILES["Satelliten_Monitor"]["sheets"]
    assert "Satelliten Monitor" in sheets
    assert "QuickScreen Ampel" in sheets


def test_p13_watchlist_profile_unchanged():
    mod = _load_hook()
    sheets = mod._PROFILES["Watchlist_Ersatzbank_Monitor"]["sheets"]
    assert sheets == ()
