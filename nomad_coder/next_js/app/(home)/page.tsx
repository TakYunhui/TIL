import { resolve } from "path";

export const metadata = {
    title: "Home",
};

const URL = "https://nomad-movies.nomadcoders.workers.dev/movies";

async function getMovies() {
    await new Promise((resolve) => setTimeout(resolve, 5000)); // getMovies 함수가 여기서 일단 멈춤
    const response = await fetch(URL);
    const json = await response.json();
    return json;
}

export default async function HomePage() {
    const movies = await getMovies();
    
    return <div>
        {JSON.stringify(movies)}
    </div>;
}