# Setting Up Work Google Drive with Custom OAuth

Your work Google Drive is blocking the default Rclone authentication. Here's how to fix it by creating your own OAuth credentials:

## Step 1: Create OAuth Credentials in Google Cloud Console

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
   - Log in with your WORK Google account

2. **Create a New Project**:
   - Click the project dropdown at the top
   - Click "New Project"
   - Name it something like "Rclone Drive Access"
   - Click "Create"

3. **Enable Google Drive API**:
   - In the search bar, type "Google Drive API"
   - Click on "Google Drive API"
   - Click "Enable"

4. **Create OAuth Consent Screen**:
   - Go to "APIs & Services" > "OAuth consent screen"
   - Choose "Internal" (if available) or "External"
   - Fill in:
     - App name: "Rclone"
     - User support email: your work email
     - Developer contact: your work email
   - Click "Save and Continue"
   - Skip adding scopes for now
   - Click "Save and Continue"

5. **Create OAuth Credentials**:
   - Go to "APIs & Services" > "Credentials"
   - Click "+ CREATE CREDENTIALS" > "OAuth client ID"
   - Application type: "Desktop app"
   - Name: "Rclone Desktop"
   - Click "Create"
   - **IMPORTANT**: Copy the "Client ID" and "Client Secret" - you'll need these!

## Step 2: Configure Rclone with Your Credentials

Once you have your Client ID and Client Secret, run:

```bash
rclone config
```

Then:
1. Choose `n` for new remote
2. Name: `workdrive`
3. Storage: `22` (Google Drive)
4. **Client ID**: Paste YOUR client ID from step 1
5. **Client Secret**: Paste YOUR client secret from step 1
6. Scope: `1` (full access)
7. Service account: [leave blank]
8. Advanced config: `n`
9. Auto config: `y`

This should work because you're using YOUR OWN OAuth app, not Rclone's default one.

## Alternative: Insync (Paid Solution)

If the above doesn't work, **Insync** is a commercial Google Drive client for Linux that works well with enterprise accounts:

- **Website**: https://www.insynchq.com/
- **Cost**: $29.99 one-time payment (no subscription)
- **Features**: 
  - Full Google Drive sync
  - Works with enterprise/work accounts
  - Multiple account support
  - Selective sync
  - Desktop integration

### Install Insync:

```bash
# Add Insync repository
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ACCAF35C

# For Ubuntu 24.04
echo "deb http://apt.insynchq.com/ubuntu noble non-free contrib" | sudo tee /etc/apt/sources.list.d/insync.list

# Update and install
sudo apt update
sudo apt install insync
```

Then run `insync start` and follow the GUI setup.

## Which Should You Try?

1. **First**: Try the custom OAuth method above (free)
2. **If that fails**: Consider purchasing Insync ($29.99)
3. **Last resort**: Contact your IT department for approved solutions

---

Let me know if you want to proceed with creating the OAuth credentials, and I can guide you through each step!
