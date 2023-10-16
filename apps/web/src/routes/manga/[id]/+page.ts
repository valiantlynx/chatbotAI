import type { PageLoad } from './$types';

export const load = (async ({ params }) => {
	const { id } = params;

	const url = `/manga/${id}`;

	const response = await fetch(import.meta.env.VITE_HOST_URL + `/api/manga/${id}?url=${url}`);
	const data = await response.json();

	return data;
}) satisfies PageLoad;
