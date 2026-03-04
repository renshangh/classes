# Building Your Own Google Drive Folder (Student Guide)

This short lab walks you through creating a personal Google Drive folder that will host all of your class materials, assignments, and recordings. We will use the **gog** skill (Google Workspace CLI) that OpenClaw provides, so you can do it from the command line.

---
## Prerequisites
1. **OpenClaw installed** on your computer (the `gog` skill is bundled).
2. **Google account** – you need a personal Gmail/Google Workspace account.
3. **OAuth consent** – the first time you run a `gog` command you will be prompted to log in and grant the CLI access to your Drive.

---
## Step‑by‑Step Instructions

### 1️⃣ Install / Verify the `gog` skill
```bash
# Verify the skill is available
openclaw skill list | grep gog
```
If it is not installed, you can add it:
```bash
openclaw skill install gog
```

### 2️⃣ Authenticate the CLI with your Google account
```bash
gog auth login
```
A browser window will open – sign in with your Google account and allow the requested permissions (Drive read/write).

### 3️⃣ Create the classroom folder structure
```bash
# Root folder for the class (feel free to rename)
gog drive mkdir "OpenClaw Classroom"

# Sub‑folders – these will be shared with the instructor later
cd "OpenClaw Classroom"
gog drive mkdir Materials Handouts Recordings
```
You should see output confirming the folder IDs.

### 4️⃣ Retrieve the shareable link
```bash
gog drive share "OpenClaw Classroom" --role reader --type anyone
```
Copy the generated URL – you will paste it into the class portal (or send it to the instructor).

---
## Verify Your Setup
Run the following to list the folder tree and ensure everything is in place:
```bash
gog drive list "OpenClaw Classroom" --recursive
```
You should see something like:
```
OpenClaw Classroom/
├─ Materials/
├─ Handouts/
└─ Recordings/
```

---
## What Next?
- Upload any class PDFs, slides, or notebooks into the **Materials** folder.
- Save your completed assignments into **Handouts**.
- If you record any practice sessions, drop the videos into **Recordings**.

When the instructor asks for your folder link, just share the URL from step 4.

---
**Troubleshooting**
- *Authentication failed*: run `gog auth login` again.
- *Permission errors*: ensure you selected the correct Google account and granted Drive access.
- *Missing command*: run `openclaw skill install gog` to reinstall.

---
*This lab is part of the OpenClaw beginner class. It demonstrates how agents can automate personal cloud setup using the `gog` skill.*
