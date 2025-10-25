# 🧩 Firebase Project Setup Guide

This guide will help you set up Firebase for your project — including downloading your service account JSON, enabling Email Authentication, and setting up Firestore.

## 🚀 Step 1: Create a Firebase Project

1. Go to the Firebase Console.
2. Click "Add project" → enter a Project name (e.g., nexora-chat-bot).
3. Disable Google Analytics if you don't need it → Click Create Project.
4. Wait until your Firebase project is ready.

## 🔑 Step 2: Generate Service Account JSON

1. Navigate to Project Settings → Service Accounts.
2. Click "Generate new private key".
3. This will download a .json file (like the one shown in your screenshot).
4. Rename the file (optional) to something like:

```
firebase-service-account.json
```

5. Place it inside your project folder, typically under:

```
/config/firebase-service-account.json
```

or

```
/server/firebase-service-account.json
```

⚠ **Important**: Never push this file to GitHub or any public repository.
Add it to your .gitignore file:

```
# Firebase service key
firebase-service-account.json
```

## 🔥 Step 3: Initialize Firebase in Your Project

If using Node.js / Express / Nest.js, install the Firebase Admin SDK:

```bash
npm install firebase-admin
```

Then initialize Firebase in your code:

```javascript
const admin = require("firebase-admin");
const serviceAccount = require("./config/firebase-service-account.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

const db = admin.firestore();
module.exports = { admin, db };
```

## 📧 Step 4: Enable Email/Password Authentication

1. In the Firebase Console, go to Authentication → Sign-in method tab.
2. Enable Email/Password under the "Sign-in providers" list.
3. Click Save.

Now users can register and log in using email and password.

## 🗃 Step 5: Set Up Firestore Database

1. In the Firebase Console, navigate to Firestore Database.
2. Click "Create database".
3. Select Start in test mode (for development).
4. Choose a location (preferably near your hosting region).
5. Click Enable.

Now you can use Firestore in your backend or frontend code:

```javascript
const usersRef = db.collection('users');

// Add a new user
await usersRef.add({
  name: "John Doe",
  email: "john@example.com",
  createdAt: admin.firestore.FieldValue.serverTimestamp(),
});
```

## 🧱 Optional: Environment Setup (Recommended)

Instead of hardcoding paths, store environment variables:

```
GOOGLE_APPLICATION_CREDENTIALS=./config/firebase-service-account.json
```

Then initialize Firebase like this:

```javascript
admin.initializeApp({
  credential: admin.credential.applicationDefault(),
});
```

## ✅ Done!

You have now:
- Created a Firebase project
- Added a service account JSON file
- Enabled Email Authentication
- Set up Firestore

You're ready to integrate Firebase services in your app 🎉