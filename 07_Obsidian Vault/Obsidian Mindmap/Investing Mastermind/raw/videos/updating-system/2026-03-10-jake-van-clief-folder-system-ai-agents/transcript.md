[00:00:00] Hi everyone, in this video we're going to dive into my concepts around folder as a workspace
[00:00:05] and architecture. What it means to use AI in a way that will actually probably last the next
[00:00:11] decade and what I think the industry is actually moving towards. Now if you've seen any of my other
[00:00:17] videos I'm sure you've seen screenshots or snippets of crazy folder structure I'm doing
[00:00:21] where I'm routing clod to different folders, my markdown files, using skills at certain times,
[00:00:27] creating animations or code with it. I have all sorts of different ways I'm doing it but I don't
[00:00:33] think I have a video out there that really dives into how I structure it and teaching you to do
[00:00:38] that. And I decided to go ahead and create a kind of template folder to walk you through all of this.
[00:00:45] This is something you could use to be able to apply to any of your workflows, build through it,
[00:00:50] understand it, and kind of explore you know building your own version of this. Now throughout
[00:00:55] this video I'm actually going to tell you a little bit about what I'm doing. I'm going to
[00:00:57] teach some concepts along the way for people who are not familiar with maybe VS Code which is the
[00:01:03] workspace I'm working in. Don't worry you don't need VS Code to do the things I'm showing you.
[00:01:07] You can do it within clod but I just want to describe like what markdown is, what it means to
[00:01:12] have an IDE, all of these things. And if you are familiar with these, you're a software engineer,
[00:01:16] you probably are. Don't worry I'm still going to be diving into the specifics and I think you're
[00:01:21] going to get a lot of out of this either way. However sometimes it's also nice to just dive
[00:01:25] back into the fundamentals.
[00:01:26] So let me paint a little scene for you. Right now most people, if they are even using AI, which fun
[00:01:31] fact about 84% of the nation is still not fully using it, but log in and use clod or chatGPT or
[00:01:37] Gemini and they're typing things. They're diving in. Maybe they get something back, they start
[00:01:44] another conversation, start over, and sometimes they're able to share context between conversations
[00:01:49] right? Like chatGPT and clod can do that. I can say you know tell me a software stack for Vigilor
[00:01:54] which is a software that I was working on for a number of years. I can say tell me a software stack
[00:01:56] for another company and it's able to go and look through our older conversations, which is nice.
[00:02:01] That's a little bit of extra there, but it's still not, you know, it's not able to look at files, have
[00:02:06] persistence, things like that. And you're constantly having to make these huge prompts. Maybe you have
[00:02:11] some sort of prompts that you save and throw in or documents and you're throwing it in and then you
[00:02:17] have to start a new conversation, throw it in, start a new conversation. You hit a wall, there's
[00:02:20] too many tokens, right? All sorts of problems there. And don't get me wrong, there's some really
[00:02:25] good prompt engineers out there.
[00:02:26] But at the end of the day, AI can only hold so much in a single information or chat area. And even further,
[00:02:35] that's not your workflow. Having to have it create a whole bunch of stuff and then re-edit it again,
[00:02:40] it's not sustainable, it's not scalable. Now for those of you who don't understand why they struggle so much,
[00:02:47] essentially AI reads everything, all of your sentence, and measures it by something called tokens.
[00:02:53] A token is roughly three quarters of a roll,
[00:02:56] word or a single word. Sometimes the word hamburger could be three tokens, ham, burr, burr, hamburger.
[00:03:03] The term comes from NLP research in the 90s. A bunch of researchers needed a unit smaller than
[00:03:10] a word because language doesn't all break the same way, right? So they borrowed token from
[00:03:16] linguistics, which borrowed it from old English token, which means a sign or a symbol. A token
[00:03:22] is just the smallest meaningful chunk of a sentence or a word.
[00:03:26] There's only so much tokens an AI can have in its context window before it starts failing.
[00:03:33] When people say context window, they mean how many tokens the AI can see at once. And that window is
[00:03:38] in fact finite. So if you dump everything into one file, an AI writing a blog post is also reading
[00:03:44] your video production notes, you're burning tokens on stuff that doesn't matter. So instead of
[00:03:49] building one big file, you want to separate your thoughts, your ideas, your work into separate areas.
[00:03:55] This is something I created for the first time in my life. I'm going to show you how to do that.
[00:03:56] For all of us, it's called a workspace blueprint. Here, you have three workspaces. And again,
[00:04:01] this is an example. You don't always have to do this, but each one handles a different kind of
[00:04:05] work. One for the community, right? Maybe I have this one for working on content and docs in the
[00:04:10] community production, right? What am I building? Where scripts? Maybe I'm creating animations,
[00:04:16] writing room. Maybe I need to have some sort of process of thinking, or I have a client list or
[00:04:21] insert as many things as I have there. And we're going to dive deeper into it.
[00:04:26] space that does the job well because you can circumnavigate and AI seeing everything and only
[00:04:32] direct it to what you want. Let me explain how that actually works though. So I'm going to show
[00:04:38] you inside of VS Code, which is an IDE, basically a developer environment that allows people to kind
[00:04:44] of look at folders in a different way. So instead of having to click into the folders like you just
[00:04:50] saw here, I can just open the folders and see everything and open the files without having to
[00:04:56] double click the files, right? So instead of having to double click this text document and
[00:04:59] opens another window, I can just bounce between them. It's much cleaner, much easier. Even if
[00:05:04] you're not into code, it looks overwhelming. I promise you all of this is just natural language.
[00:05:08] This literally reads like a document. So this is a markdown file. If you haven't seen them before,
[00:05:13] markdown is just a text file with some lightweight formatting, right? You have dashes for bullets,
[00:05:19] you have hashtags or pound symbols, if everyone else remembers when they were just called that,
[00:05:24] for headers.
[00:05:26] You have all sorts of stuff like asterisks for bolding or doing things in that way. And there's
[00:05:31] a lot of programs that can actually run this to look a certain way. In fact, your Claude does
[00:05:37] exactly that. If you look, when you're talking to an AI, it's writing in markdown already. These
[00:05:42] boldings, these lines, all of these things, watch what happens when I copy this. All of that
[00:05:48] formatting disappears when I paste it into here and it turns into markdown because that's how
[00:05:56] it works. Markdown is just a good way to format text. If you're curious, there's a man named John
[00:06:00] Gruber. He actually created this in 2004. The whole idea was write something that's readable as
[00:06:06] plain text, but can also render into a formatted document. He named it markdown as a play on markup
[00:06:14] language, which is the same stuff that HTML, right? The stuff that builds websites, hypertext
[00:06:21] markdown language. And all it does is mark stuff down with tags. Markdown strips all of that stuff.
[00:06:25] Sucks all the tags and absurdity away and makes it look like something simple like this. But again,
[00:06:31] you're probably not here for this. You're here for the file system. So let's move on to that
[00:06:35] next step. So in this specific folder, which is an example, it runs on essentially three layers.
[00:06:42] And there's a reason for each one. If you look at my Claude MD, my Claude markdown file, this is
[00:06:49] something that my AI will read every time it's in any one of these folders. So this is something
[00:06:54] that the AI will always have. And that's what I'm going to do here. I'm going to go ahead and
[00:06:55] have and always reads. Imagine it's you're just copying and pasting this into Claude code or into
[00:07:02] Claude every time you open it. Now you can actually just type in to Claude, read the Claude.md. In this
[00:07:08] case, it's Claude code. You could be working inside of Claude co-work as well, which is again,
[00:07:14] a video I have on how to install, and it can operate inside of folders in case the VS code
[00:07:19] is too much for you. But just read the Claude.md and tell me what this is. Before you had to copy
[00:07:25] and paste,
[00:07:25] do all these things, it had to read the every file that's in here. In this case, it reads the
[00:07:31] Claude.md and immediately without having to read everything else, understands the product, the
[00:07:36] process, what's going on, my writing room, my production, my community, it knows where to find
[00:07:41] it, what the file names are, all from just a single text prompt that allows it to understand
[00:07:47] where to go, what to do, what are these areas. But let me describe this a little simpler for
[00:07:52] those of you who might, you know, feel like this is a bit over.
[00:07:55] Well, layer one in this is the map. This is what loads automatically, right? It's looking at it.
[00:08:03] So you put the stuff that agent always needs to think about folder structure, naming conventions,
[00:08:09] where files go. Think of this as the floor plan. You walk into any room, the floor plan is on the
[00:08:16] wall and the agent knows where to go. Now layer two is where the floor pan tells you to go. It's
[00:08:23] the actual rooms. What?
[00:08:25] Is your task. Go here. I want to write a blog post. Well, then you need to go to here and read
[00:08:32] this context or this Markdown file. If you want to build a demo or a video, you need to go here and
[00:08:39] read this context or Markdown file. And this could be one that you wrote by hand, or it could be one
[00:08:44] that you told Claude to wrote. And we're going to dive into that here shortly. Layer three is
[00:08:49] the actual workspace itself. Where do you want your files going? What content are you doing?
[00:08:55] If you're writing stuff, where do you want the events to be? Where do you want newsletters to be?
[00:09:00] Where do you want social to be? And it's just a file system. Again, if you don't want to work
[00:09:04] inside of here, you can actually just go straight into the folder and just create new folders,
[00:09:10] new text document. That can be a prompt that can be a context, right? It's that simple. And you can
[00:09:16] just, you can just edit it without any of this. Look, my, uh, my Claude dot MD. This is what it
[00:09:21] looks like in, if you open up notepad, same thing and nothing breaks when you edit it,
[00:09:25] you can type whatever you want in here. It's just English. Now it's good to have it uniform and
[00:09:31] well, but that's the idea here. Most people are only doing one of these layers, maybe two.
[00:09:36] The reason you want to actually have these three layers is it stops the narrow funnel
[00:09:43] of AI doing too much all at once without allowing you to edit every single part,
[00:09:48] but still give you the ability to automate the entire process. So again, the router,
[00:09:54] the initial Claude,
[00:09:55] the MD or whatever you're naming it is loaded. When you start any task, the workspace is loaded
[00:10:02] when you're in the workplace, when you want to do production, it's only reading stuff that's
[00:10:07] in production as it needs to. When you're doing stuff in the writing room, it's only writing it
[00:10:11] when you're in the writing room, for example, go to writing room. Let's start making something
[00:10:19] very little prompting, almost terrible prompting yet the agent without wasting
[00:10:25] a whole bunch of coke ins and going through everything immediately goes to the context file
[00:10:30] that I have in writing room that describes what it is, describes what to load and what not to load
[00:10:36] and just describes the folder structure and what the process is. First, I understand the topic,
[00:10:40] then I find the angle, then I write it, then I catch problems. You can also incorporate skills
[00:10:46] into this, right? So you can download the humanizer skill, which is an actual GitHub.
[00:10:50] I recommend you all check out or like doc co-authoring skill, which is another set
[00:10:55] of markdown files or even Python scripts and tutorials that someone else build to do a certain
[00:11:01] task. And this is where this whole process is different than just running skills. You're
[00:11:06] putting skills inside of a thought process. And as you can see right here, we're in the writing room,
[00:11:11] clean slate, no drafts in progress. Voice is loaded. Style is blog posts. What do you want
[00:11:15] me to make from one single prompt? We've gotten it in there, but while that's going on, I can
[00:11:21] open up another Claude and I can say, Hey, I want to.
[00:11:25] Do some work in production. And it's going to go in there and I can do whatever work I want to do in
[00:11:31] production, right? I want to maybe make some designs. I want to create some sort of code for
[00:11:36] workflows in there. But the real fun happens is when you're building stuff in production with one
[00:11:41] of your Claude code instances, you're writing a script and you can say, Hey, take the script
[00:11:47] from writing room and let's make an animation out of it in production.
[00:11:54] It's moving.
[00:11:55] That file.
[00:11:56] It's going to go there now.
[00:11:57] It's going to notice that I don't have any scripts in there when I send this out.
[00:12:00] But if I did have a final in there, it's going to go look for it, right?
[00:12:03] There's no scripts.
[00:12:04] Boom.
[00:12:04] It didn't waste a whole bunch of tokens.
[00:12:06] It didn't do anything, but it immediately knew, oh, well, we have to write a script first.
[00:12:09] Or if you have a script somewhere else, you can upload it.
[00:12:11] You see most apps or frameworks or agentic things require you to build an agent for each of these.
[00:12:17] I need a writing room agent.
[00:12:18] I need this agent.
[00:12:19] I need this agent.
[00:12:20] But the way in which you approach each task is always different.
[00:12:24] Why not?
[00:12:24] Just have.
[00:12:25] Claude code become the agent you need when you're working in the workspace.
[00:12:30] And you see from there you get the most important part of this process is just good routing in English language.
[00:12:38] Again, this is all just English, right?
[00:12:40] File folder names, titles.
[00:12:42] It's describing what you want, right?
[00:12:44] This right here is the most important pattern in the whole system.
[00:12:47] It's just a simple table that tells the AI for this task.
[00:12:52] Read these files.
[00:12:53] Skip.
[00:12:54] Those.
[00:12:54] Files.
[00:12:55] You might need these skills without this.
[00:12:57] The AI either reads everything and runs out of the room and just does all sorts of stuff.
[00:13:02] You don't want it to do using way too many tokens or it guesses wrong about what matters or just doesn't hit what you need.
[00:13:09] Or you can't edit what it creates along the process.
[00:13:12] This table eliminates all of those problems.
[00:13:14] This the system here gets rid of all of that.
[00:13:17] Now, let's go ahead and zoom in a little bit here and actually really look at this kind of folder structure.
[00:13:22] Walk through this pipeline.
[00:13:24] Imagine you're sitting here and you open up production and you go to workflows, right?
[00:13:29] So, you know, you're doing some sort of animation production or insert whatever it is that this folder is as a separate workspace as part of a larger tasks flow that you're doing.
[00:13:39] Production has a pipeline in itself as well.
[00:13:43] Four stages.
[00:13:44] You have to do a brief.
[00:13:45] You need a spec with a specification of build and an output.
[00:13:49] I have a brief some sort of script that I want to do.
[00:13:52] I have a spec.
[00:13:53] That's generated.
[00:13:54] From that brief, and then it goes into the builds and it builds out the animations.
[00:13:57] And then finally, you have the output.
[00:13:59] More importantly, this allows me to have one MD file, right?
[00:14:03] So for my production, I can have a ton text for this file system that is generating different types of sub agents or ways to look at it again.
[00:14:11] I'm not even worried about agents.
[00:14:12] I'm just worried about what the workspace is, what I want to do in these workspace.
[00:14:17] If I want to understand, look up technical standards, look up design rules.
[00:14:21] I can find that because I might.
[00:14:24] Have that in a dock, right?
[00:14:25] So I have components or maybe some way.
[00:14:27] I like to design these systems with my color designs, my headers, my quality.
[00:14:33] And again, these are all just generated from English super short Docs.
[00:14:36] These are visual philosophy or what type of tech you want to use and it doesn't always have to read that.
[00:14:42] But maybe during the brief stage, it does right when you're sitting there and you're going through and you're looting the brief.
[00:14:49] Well, I need to make sure you look at this text standards when you're making the brief if it's loading the spec.
[00:14:54] I need to make sure it looks at the design system and our component library and then maybe it doesn't need to load the deck as well.
[00:14:59] And you can swap this around super easily just by looking at it.
[00:15:03] This is traditional function calling software routing.
[00:15:07] This is existed for decades and decades, but now it gets to be natural language English.
[00:15:14] Now at this point many of you are like, oh, well, you're just making a bunch of skills.
[00:15:17] Technically.
[00:15:18] Yes.
[00:15:19] Now for those of you who don't know what skills are again, I mentioned them earlier.
[00:15:22] I talked about this idea.
[00:15:23] You can download them from everywhere.
[00:15:25] There's PowerPoint skills and I have other videos on this.
[00:15:30] But at the end of the day skills are a process that someone else figured out and designed a set of packages or folders.
[00:15:38] Just like I'm doing here to tell Claude how to do something thing is skills.
[00:15:42] Aren't just markdown files with instructions.
[00:15:44] Some are just that but skills Burke best when they're wired into a system.
[00:15:49] One important note to is this is where the difference between.
[00:15:53] It's just skills.
[00:15:54] We're creating here and it's a system.
[00:15:56] You're actually putting skills inside of your MD.
[00:16:00] So in this case, I have in my context for production.
[00:16:04] I have the fire Outlook what I want to do, but also right.
[00:16:08] This is where you can call to call skills or MCP servers.
[00:16:13] If you don't know what an MCP model context protocol.
[00:16:17] I think that deserves an entire video in itself, but just think of it as a way that the AI can talk to other.
[00:16:23] Apps and services easier.
[00:16:25] It's designed to just kind of plug and play it in rather than you have to create all these custom integrations at certain points.
[00:16:31] We might want the front-end design skill or a web app testing skill or PDF skill,
[00:16:35] or I might want to give Claude the opportunity to look up a skill find a new skill or even possibly create one.
[00:16:45] You can wire up to 15 skills 20 skills a hundred skills into a workspace or you can perfectly.
[00:16:52] Add the skills where you would need them inside the workspace rather than having them loaded at all times.
[00:17:00] That's the whole idea here is about plug-and-play and routing one other sneaky thing.
[00:17:05] I do to like completely ignore like databases or anything like that in my Claude MD the main file at the beginning that shows,
[00:17:14] you know, every AI or every agent that comes into this workspace can see my entire folder structure and navigation.
[00:17:20] I just add naming conventions, right?
[00:17:22] So if a file is going to be outputted a certain way, it needs to name it for blog drafts.
[00:17:28] It needs to be like file name where it's at.
[00:17:31] Is it draft?
[00:17:31] Is it v2?
[00:17:32] Is it v3 example API off guide draft right or same for newsletters?
[00:17:37] Here's the year and day and then here's what it's kind of is right?
[00:17:41] Twenty twenty six zero three launch week dot MD.
[00:17:44] So the AI knows to organize and move stuff which comes in handy when instead of having to navigate through these files or have an agents.
[00:17:52] That's connected.
[00:17:52] To some sort of, you know, SQL database or vector database or query or Postgres or anything like that.
[00:17:59] I could just say, hey, pull my off demo.
[00:18:07] Demo v2 and build a spec from it.
[00:18:11] It immediately knows without me doing anything to look where that v2 demo script would be because it knows how to find it.
[00:18:19] It knows to pull it.
[00:18:20] Then it knows to read.
[00:18:22] The Docs associated with specs and then start building it.
[00:18:27] I have zero code.
[00:18:29] Technically speaking running any sort of python injection or framework or database.
[00:18:35] This is tools that people are building right now.
[00:18:38] They're building apps and crazy python stuff, which in some very bespoke cases might be useful.
[00:18:43] But most of the time for most people you don't need all that extra stuff to get the process and the job done the job to be done is more.
[00:18:52] Important than this kind of rigid architecture that so many people are building.
[00:18:57] You see the folder becomes your app.
[00:18:59] This is your UI.
[00:19:01] What's simpler UI than a folder and the best part is I don't even need to technically click on anything.
[00:19:06] I could just talk with my voice to AI have it do all the text work for me.
[00:19:11] The next stage of this I promise you within six months.
[00:19:15] Everyone's going to be doing this is just talking to your folder set up.
[00:19:19] It's going to be designed and set up to be this way.
[00:19:22] It's going to be around yours, which leads into a good final point.
[00:19:26] How do you make this yours?
[00:19:28] This template uses a fake idea with fake process, right?
[00:19:32] Fake blog posts and demos.
[00:19:35] If you're a content creator writing room might become your script lab production becomes your edit Bay.
[00:19:42] Whatever Community becomes a distribution hub and you're going to remove and change these rules to edit your platform.
[00:19:49] Maybe your tone and voice.
[00:19:51] Inside of these right?
[00:19:53] So what is your audience?
[00:19:55] That's what you want to hear.
[00:19:56] It's working developers two to eight years of experience technical decision-makers developer ad.
[00:20:01] It might be something completely different.
[00:20:03] You might be in construction or real estate, but this is roughly what you would be doing all of them.
[00:20:10] And the best part is all you need is one subscription to Claude code
[00:20:13] and you can generate a hundred quote-unquote apps that are just folders creating what you need.
[00:20:20] Obviously.
[00:20:21] It's much more complicated.
[00:20:23] Once you get into breaking down your workflow, but if you're a developer, if you're a freelancer, right?
[00:20:29] Just swap design for engineering and Docs or intake and production and delivery, right?
[00:20:35] This workspace changes lightly, but the three-layer routing system the idea that you go from hey, look at this area.
[00:20:45] This is what you're going to to lower level context ones to lower level skills.
[00:20:51] Is the idea here.
[00:20:53] It's just layer.
[00:20:54] This isn't a prompt tricked.
[00:20:56] This isn't some sort of crazy infrastructure.
[00:20:59] It's folders and Markdown files with the understanding of advanced software engineering every conversation after that the AI knows where it is
[00:21:09] what to load what tools to use and where to put the work in now.
[00:21:13] There is a lot of history behind my thinking.
[00:21:16] I didn't just randomly come up with this and there's a lot of people who are already doing this.
[00:21:20] And the reason they're.
[00:21:21] Doing this is because it works.
[00:21:23] I'm writing a very large research paper right now that goes into the history of programming rules of transparency rules of composition all the way back down to 1972.
[00:21:32] And then I'm bringing it forward and applying all this stuff to modern-day AI what it means to have humans in it.
[00:21:39] And I specifically talk about the layers that we could actually have and I actually go into a five-layer architecture in the paper.
[00:21:45] But realistically most of you just need to understand the three main layers that we talked about here.
[00:21:49] I will be making videos.
[00:21:51] On this.
[00:21:51] However, it is in the main chat.
[00:21:54] If you want to download this and give it to Claude so that it can tell you about it rather than having to read through it.
[00:22:00] I highly recommend that.
[00:22:01] In fact, I urge you to do it because some of this is kind of technical information.
[00:22:05] I'm being nerdy.
[00:22:06] I'm being structured in it, but this is layering out what the next decade is looking like and this isn't because I'm predicting the future.
[00:22:14] It's because I'm learning from the past from the last 200 years of software engineering.
[00:22:20] And I mean 200 when I say that and applying it to AI.
[00:22:25] I want to teach the concepts that last not the concepts that are replaced next month.
[00:22:30] I understand that some of this might be in a little fast.
[00:22:32] It might be a little confusing.
[00:22:33] I'll keep making deeper dives.
[00:22:35] Give me feedback on what you didn't understand.
[00:22:38] How did I move too fast?
[00:22:40] I want to make these better every day again.
[00:22:42] I'm making these on my own.
[00:22:43] So hopefully this all gave you a good idea.
[00:22:46] If you do want access to any of these files or worker template.
[00:22:50] I am giving them already to my VIP and my premium accounts.
[00:22:56] It's my one way of like the work right to be able to support this.
[00:22:59] So if you're able to subscribe amazing if it actually is that much of a financial challenge, please reach out to me.
[00:23:06] I can try to see if I can get you something, you know quick and easy for you.
[00:23:09] But at the end of the day go go check it out.
[00:23:12] Go check out all my other courses that I'll be doing and again as always happy learning.
