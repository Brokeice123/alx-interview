#!/usr/bin/env node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.error('Please provide a movie ID as the first argument.');
    process.exit(1);
}

// URL to fetch the movie details
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching the film:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to fetch film. Status code: ${response.statusCode}`);
        process.exit(1);
    }

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    // Function to fetch and print character names sequentially
    const fetchAndPrintCharacter = (index) => {
        if (index >= characterUrls.length) {
            return;
        }

        request(characterUrls[index], (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error fetching character:', charError);
                return;
            }

            if (charResponse.statusCode !== 200) {
                console.error(`Failed to fetch character. Status code: ${charResponse.statusCode}`);
                return;
            }

            const characterData = JSON.parse(charBody);
            console.log(characterData.name);

            // Fetch the next character in the list
            fetchAndPrintCharacter(index + 1);
        });
    };

    // Start fetching characters from the beginning of the list
    fetchAndPrintCharacter(0);
});
