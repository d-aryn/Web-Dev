# Album Browser

Lab 6: Routing & HTTP — Angular app that browses albums and photos from [JSONPlaceholder](https://jsonplaceholder.typicode.com).

## Run the project

```bash
npm install
npm start
```

Open http://localhost:4200

## Build

```bash
npm run build
```

## Routes

- `/home` — Welcome page
- `/about` — About page
- `/albums` — List of albums
- `/albums/:id` — Album detail (view/edit title)
- `/albums/:id/photos` — Photos for an album

## Tech

- Angular (Router, HttpClient)
- JSONPlaceholder API for albums and photos
