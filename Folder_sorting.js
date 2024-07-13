import fs from 'fs/promises';
import path from 'path';

const filepath = 'C:/Users/Aliyas/Downloads';

async function listfile(directory) {
  const files = await fs.readdir(directory);
  for (const file of files) {
    
    const fileextension = file.split('.').pop(); // Get the file extension
    let newpath = path.join(directory, fileextension);

    // Ensure the directory exists
    await fs.mkdir(newpath, { recursive: true });

    const source = path.join(directory, file); // Correctly join the source file path
    const destination = path.join(newpath, path.basename(file)); // Correctly join the destination file path

    // Move the file
    await fs.rename(source, destination);
    console.log(fileextension)
  }
}

listfile(filepath);
