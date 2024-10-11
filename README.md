# momochat-translations
Translation collaborative work for MomoChat.

## Workflow
1. Edit character data/translations in
[Google Drive](https://drive.google.com/drive/folders/1qxfh_hbGerl2c7Pe6grcA2EIAsOLxjVM?usp=drive_link).

2. Run this
[Apps Script](https://script.google.com/d/1NFEqLrE-Vp3fEjTvtEd-KbuBBbolX4T6Gc9Cl0rLEw7CDu5DAm_3bU5K/edit?usp=sharing)
to export all files as CSV files into a temporary folder (MomoChat Database Export) in your Google
Drive.

3. Fork this repo and update the CSV files with the ones in your Google Drive.

4. Create a pull request to update the translation files. Wait for it to be accepted.

5. Trigger the
[upload-csv action](https://github.com/momo-jisan/momochat-translations/actions/workflows/upload-csv.yml)
to upload the CSV files to the database.
