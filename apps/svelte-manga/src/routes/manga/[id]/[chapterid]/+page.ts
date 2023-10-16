import type { PageLoad } from './$types';

export const load = (async ({ params, fetch }) => {
	const { id, chapterid } = params;
	const url = `/manga/${id}/${chapterid}`;

	const response = await fetch(
		import.meta.env.VITE_HOST_URL + `/api/manga/${id}/${chapterid}?url=${url}`
	);
	const data = await response.json();
	return data;
}) satisfies PageLoad;
