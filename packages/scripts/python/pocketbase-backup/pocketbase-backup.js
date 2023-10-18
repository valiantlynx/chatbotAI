// Import and configure dotenv to load environment variables
import 'dotenv';
import PocketBase from 'pocketbase';

const pocketbaseUrl = process.env.POCKETBASE_URL;
const adminEmail = process.env.POCKETBASE_ADMIN_EMAIL;
const adminPassword = process.env.POCKETBASE_ADMIN_PASSWORD;

if (!pocketbaseUrl || !adminEmail || !adminPassword) {
  console.error('Environment variables not set correctly.');
  process.exit(1);
}

const pb = new PocketBase(pocketbaseUrl);

async function main() {
  try {
    // Authenticate as an admin
    await pb.admins.authWithPassword(adminEmail, adminPassword);

    // Create a new backup
    await pb.backups.create('new_backup.zip');

    console.log('Backup created successfully.');
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
