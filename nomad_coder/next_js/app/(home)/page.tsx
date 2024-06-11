import Link from "next/link";
import { resolve } from "path";

export const metadata = {
    title: "Home",
};

export const API_URL = "https://nomad-movies.nomadcoders.workers.dev/movies";

async function getMovies() {
    // await new Promise((resolve) => setTimeout(resolve, 1000)); // getMovies 함수가 여기서 일단 멈춤
    const response = await fetch(API_URL);
    const json = await response.json();
    return json;
}


export default async function HomePage() {
    const movies = await getMovies();

    return (<div>
        {movies.map((movie) =>
            <li key={movie.id}>
                <Link href={`/movies/${movie.id}`}>
                    {movie.title}
                </Link>
            </li>)
        }
    </div>
    );
}