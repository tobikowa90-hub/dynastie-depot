[00:00:00] Boris Churney, the creator of Claude Code, just dropped the source on how he's using
[00:00:03] Opus 4.7.
[00:00:04] He's been working with it for weeks before the rest of us got our hands on it, and he
[00:00:08] said that Opus 4.7 feels more intelligent and precise, but it took a few days for him
[00:00:13] to learn how to work with it effectively.
[00:00:15] The guy who built it had to re-learn it.
[00:00:18] So what hope did the rest of us have if we just port over our old prompts?
[00:00:22] That's why I spent hours looking into every single post and comment Boris made since the
[00:00:27] release of Opus 4.7.
[00:00:28] I've tested every single one of his tips, so let me walk you through the new 6-step
[00:00:32] system Boris uses to 3x Claude's output.
[00:00:35] Oh, and if we haven't met yet, I'm Duby.
[00:00:37] I run multiple Claude Code agents 24x7 inside an autonomous app factory, and I made over
[00:00:42] $47,000 vibe coding in less than 50 days.
[00:00:44] When Claude releases an update, my token bills tell me before Anthropic even makes the announcement.
[00:00:49] Every single principle in this video is something a complete beginner can apply.
[00:00:53] No coding background required.
[00:00:54] So let's start with Boris' favorite new feature, Auto Mode.
[00:00:57] Auto Mode equals no more permission prompts.
[00:00:59] Opus 4.7 loves doing complex, long-running tasks, like deep research with factoring code,
[00:01:05] building complex features, iterating until it hits a performance benchmark.
[00:01:09] In the past, you either had to babysit the model while it did these long tasks or used
[00:01:13] dangerously skipped permissions, so they rolled out Auto Mode as a safer alternative.
[00:01:17] In this mode, permission prompts are routed to a model-based classifier to decide whether
[00:01:21] the command is safe to run.
[00:01:22] If it's safe, it's auto-approved.
[00:01:24] Not only does this mean no more babysitting, but it also means you can run more Claude's
[00:01:28] in parallel.
[00:01:29] Once a Claude is cooking, you can switch focus to the next Claude.
[00:01:32] Simply use the shortcut Shift plus tab inside of the Claude code terminal or toggle it from
[00:01:36] the dropdown in the app.
[00:01:37] This feature is currently only available for max tier users.
[00:01:40] If you're on the pro plan, don't worry, I show you an alternative later in the video.
[00:01:44] I tested it out yesterday.
[00:01:45] I had Claude code review my entire code base for an app I'm building.
[00:01:48] Usually, I'm glued to my screen, clicking yes every time I make a tool call.
[00:01:52] However, this time round, it didn't even ask for a single permission.
[00:01:54] I went to make a coffee, came back, and it's already completed the task.
[00:01:58] But Auto Mode only works if the model is actually making good decisions under the hood.
[00:02:02] So let me tell you about Boris's next tip.
[00:02:04] Effort levels.
[00:02:05] Now, I couldn't find which benchmark measured this, but Anthropic has once again taken the
[00:02:09] lead from Codex with 5 effort levels to choose from.
[00:02:13] Yep, there's a new effort level.
[00:02:16] It's called Extra High, which is now the default for Claude code.
[00:02:19] So if you recently updated your Claude, you might be wondering why your token usage may
[00:02:23] have gone up.
[00:02:24] This is likely why.
[00:02:25] It sits between high and max and is the new default effort level, up from medium.
[00:02:29] Boris mentions Opus 4.7 uses adaptive thinking instead of thinking budgets.
[00:02:33] To tune the model to think more or less, he recommends tuning effort.
[00:02:37] Use lower effort for faster responses and lower token usage.
[00:02:40] Use higher effort for the most intelligence and capability.
[00:02:43] Each effort level used to come with a guardrail on how long Claude was allowed to work for.
[00:02:47] Lower efforts usually meant it could work on the task for a few minutes or the way up
[00:02:51] to max effort, which could run for a few hours.
[00:02:54] However, now the model decides how long to take based on how hard the step actually is.
[00:02:59] The only thing you can actually change now is the effort.
[00:03:02] Most people think max is smarter.
[00:03:04] Max is actually less consistent.
[00:03:06] Anthropic's own blog post said it's prone to overthinking with diminishing returns.
[00:03:10] They are literally telling you to use extra high, not max.
[00:03:14] Something Boris says he personally uses extra high effort for most cars and max effort for
[00:03:18] the hardest task.
[00:03:20] Use slash effort in the terminal or toggle it from the drop down.
[00:03:23] I did some tests and I wouldn't recommend dropping below high if you're vibe coding.
[00:03:27] Lower and medium seem to skip reasoning and takes a lot of shortcuts.
[00:03:29] Notice the pattern with everything we just covered?
[00:03:31] They all run on your laptop, which means the best Claude settings in the world only work
[00:03:37] while you're awake.
[00:03:38] Shut the lid, agents dead.
[00:03:39] That's exactly what Hermes agent solves.
[00:03:42] Built by Noose Research, it runs on its own infrastructure with a built in learning loop
[00:03:46] that actually gets smarter over time.
[00:03:48] But Hermes still needs to live somewhere.
[00:03:51] Running it on your laptop defeats the purpose because the moment you close your screen,
[00:03:55] your self-improving agent stops improving.
[00:03:57] You need it online 24-7 under your control.
[00:04:01] That's where Hostinger comes in.
[00:04:02] With Hostinger's VPS, you get a one-click docker template that deploys Hermes agent
[00:04:06] in seconds.
[00:04:07] You don't need to know any code.
[00:04:08] It just works.
[00:04:10] API keys and conversation data stay on your server, not some third parties.
[00:04:15] Because it's a VPS, your agent runs 24-7 and never loses its memory, even through restarts.
[00:04:19] And it plugs straight into Telegram, Slack, Discord or WhatsApp, so you can talk to it
[00:04:23] using your phone.
[00:04:24] If you want to spin up your own self-improving AI agent, use my link below and use code doobiebooby
[00:04:29] for an exclusive discount.
[00:04:31] Shout out Hostinger for sponsoring this video.
[00:04:33] Okay, so Automode handles permissions, Extra High handles depth.
[00:04:36] Now let me show you how the creator of Claude code doesn't even watch your work anymore.
[00:04:40] This one genuinely surprised me.
[00:04:42] He said,
[00:04:43] I've been loving the new focus mode in the CLI, which hides all the intermediate work
[00:04:47] to just focus on the final result.
[00:04:49] The model has reached a point where I generally trust it to run the right command and make
[00:04:53] the right edits.
[00:04:54] He just looks at the final result.
[00:04:55] Why does this matter?
[00:04:56] Because every Claude code tutorial for the last 12 months has been about watching the
[00:05:01] plan, reviewing every step, correcting when it wanders, Boris is saying, stop.
[00:05:06] Focus mode hides the intermediate steps so you only see the output.
[00:05:09] To be totally honest though, I don't fully agree with this take.
[00:05:12] So here's my middle ground that's been working.
[00:05:15] Focus mode on for my builder agents.
[00:05:16] I don't need to watch a builder type out strings of code.
[00:05:19] Focus mode off for my reviewer agent.
[00:05:21] I want to see their reasoning because it lets me know that my prompt worked and that they're
[00:05:25] on the right track.
[00:05:26] And don't worry, if focus mode hides something you actually need, every session still saves
[00:05:30] the full log.
[00:05:31] You can scroll back if the output looks off.
[00:05:33] I'm coining the combination of focus mode plus auto mode as ghost mode because you literally
[00:05:39] won't see anything until it's already done.
[00:05:41] Just type slash focus to toggle between on and off.
[00:05:44] So far with killed commissions, tuned depth, hidden noise, this next one takes that even
[00:05:49] further.
[00:05:50] It literally scans your sessions and builds your list.
[00:05:53] It's called fuel permission prompt skill and Boris has vouched for this skill personally.
[00:05:58] He says that the new skill scans through your session history to find common bash and mcp
[00:06:02] commands that are safe but cause repeated permission prompts.
[00:06:05] It then recommends a list of commands to add to your allow list.
[00:06:08] You just run the skill and it looks at every command Claude keeps asking you permission
[00:06:12] for, figures out which ones are safe, builds you a whitelist, you approve it and it will
[00:06:15] never ask permission for those again.
[00:06:17] This is a great alternative to my pro plan users who don't have access to auto mode.
[00:06:21] I recommend run it once a week and see what it picks up on.
[00:06:24] One thing I noticed when testing that Boris doesn't really mention is that this is actually
[00:06:28] a great way to find patterns and deepen your understanding of how you work.
[00:06:32] Because the best way to utilize AI for your own personal gain is to understand what repetitive
[00:06:37] tasks you can automate within your workflow.
[00:06:40] So that's four settings that handle friction.
[00:06:42] The next one is the setting that handles the pain of coming back to a long session.
[00:06:46] Recaps.
[00:06:47] This new feature shipped earlier last week.
[00:06:49] Boris describes recaps as short summaries for what an agent did and what's next.
[00:06:53] Very useful when returning to a long running session after a few minutes or a few hours.
[00:06:58] After a long session the model auto generates a summary.
[00:07:00] But when you come back two hours later you're not scrolling through your entire chat history
[00:07:04] to figure out where you left off.
[00:07:06] So let's shift this specifically to prep for the 4.7 because the whole point of 4.7 is
[00:07:11] long running work.
[00:07:12] Overnight refactors.
[00:07:13] Multi hour sessions.
[00:07:14] Out of all of Boris's tips in this video, this is actually my personal favorite.
[00:07:18] I'm sure you guys know the pain when you're running multiple agents at the same time.
[00:07:22] One is easy to manage.
[00:07:23] But when you get to 3, 5, sometimes 10 you start forgetting what each agent was even
[00:07:27] working on.
[00:07:28] So recaps has actually been a huge help for me personally.
[00:07:32] One thing I did notice while using it is recaps can compress away any errors you would
[00:07:37] have caught by scrolling.
[00:07:38] If your agent did anything weird, still skim through the raw log.
[00:07:42] The feature is automatically implemented into Opus 4.7 but if you want to turn it off you
[00:07:46] can do so in slash configs.
[00:07:48] 5 settings down.
[00:07:49] Now let me show you Boris's advice for 3x in Claude's output.
[00:07:52] Boris's prompt style plus the slash go skill.
[00:07:55] Personally many of my prompts these days look like Claude do blah blah slash go.
[00:07:59] That's it.
[00:08:00] That's his format.
[00:08:01] Claude's in a slash command.
[00:08:02] Claude do blah blah slash go.
[00:08:05] Nah, but I'm not serious.
[00:08:08] What does slash go even do?
[00:08:10] He built a skill 3 steps chained into one command.
[00:08:13] 1.
[00:08:14] Enter n testing using bash, the browser or computer use.
[00:08:17] Claude actually runs the thing and checks it works.
[00:08:20] 2.
[00:08:21] Slash simplify.
[00:08:22] Another skill that cleans up the code removes dead paths, trims what he calls over engineering.
[00:08:26] 3.
[00:08:27] Submits a pull request, packaged, labeled and done.
[00:08:30] 1.
[00:08:31] 3 jobs.
[00:08:32] No supervision required.
[00:08:33] Is Claude on why this matters?
[00:08:35] Verification is important because that way when you come back to a task you know the
[00:08:39] code works.
[00:08:40] Boris isn't writing 400 word prompts anymore, he's writing 10 word prompts and chaining skills
[00:08:45] for everything else.
[00:08:46] The skill does the heavy lifting.
[00:08:48] And this ties the entire video together because auto mode handles permissions, extra high
[00:08:51] handles depth, focus mode hides noise, fuel permission prompts kills the friction, recaps
[00:08:56] handles memory and slash go handles verification.
[00:08:59] That's the full loop.
[00:09:00] You can build your own slash go skill through Claude code because it has skill development
[00:09:04] built in.
[00:09:05] The point Boris is trying to make here is stop typing the same instructions over and
[00:09:09] over.
[00:09:10] Package them.
[00:09:11] If you want to build your own slash go skill just copy paste this prompt.
[00:09:14] So let's recap Boris Choney's full 4.7 system.
[00:09:17] First you've got auto mode, shift tab to enable, stop clicking permissions and just
[00:09:21] let it run.
[00:09:22] 2.
[00:09:23] You've got effort level.
[00:09:24] Extra high is the new default now so stop running max everywhere, bump up the hard steps,
[00:09:27] drop back down when you don't need it.
[00:09:29] 3.
[00:09:30] You've got focus mode.
[00:09:31] Hide intermediate work, trust the output of builders not reviewers.
[00:09:34] 4.
[00:09:35] You've got slash fuel permission prompts skill, run it once, approve the list, kill repeated
[00:09:39] prompts forever.
[00:09:40] 5.
[00:09:41] You've got recaps, come back to long sessions with a summary.
[00:09:44] 6.
[00:09:45] We found out Boris's prompt format is literally just Claude do blah blah slash go, package
[00:09:49] your verification into a skill, use short prompts and let skills do the heavy lifting.
[00:09:54] Do those 6 things and you're running Claude code the way the guy who built Claude code
[00:09:58] runs it.
[00:09:59] Now if you actually want to see what this looks like when you scale it up, I wired all
[00:10:02] 6 of these principles into an autonomous app factory with 11 agents running 24x7.
[00:10:07] Full architecture breakdown right here, combine this video with that one and you will become
[00:10:12] a vibe coding savage.
[00:10:14] Peace.
