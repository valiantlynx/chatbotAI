import type { RequestHandler } from './$types';
import axios from 'axios';
import cheerio from 'cheerio';

export const GET: RequestHandler = async ({ url, setHeaders }) => {
	const souceUrl = url.searchParams.get('url');
	setHeaders({
		'Access-Control-Allow-Origin': '*',
		'Cache-Control': `public, s-maxage=${60 * 60 * 24 * 365}`
	});

	// Your logic for handling the page parameter and generating the response
	try {
		const url = `${import.meta.env.VITE_IMAGE_URL}${souceUrl}`;

		const response = await axios.get(url);

		const $ = cheerio.load(response.data);

		const titleElement = $('.story-info-right h1');
		const imgElement = $('.info-image img');
		const descriptionElement = $('#panel-story-info-description');

		// Select the parent element containing the author information
		const authorContainer = $('.table-value');
		const lastUpdated = $('.stre-value').text();
		// Extract the last update date and time
		const lastUpdatedPattern = /(\w{3} \d{1,2},\d{4} - \d{2}:\d{2} [APM]{2})/;
		const lastUpdatedMatch = lastUpdated.match(lastUpdatedPattern);
		const lastUpated = lastUpdatedMatch ? lastUpdatedMatch[1] : '';

		// Extract the view count
		const viewCountPattern = /([0-9]+[A-Z])/;
		const viewCountMatch = lastUpdated.match(viewCountPattern);
		const viewCount = viewCountMatch ? viewCountMatch[1] : '';

		// Select all the anchor elements within the parent container
		const authorElements = authorContainer.find('a');

		// Create an array to store the extracted author names
		const authors: string[] = [];

		// Iterate through the anchor elements and extract their text content
		authorElements.each((index, authorElement) => {
			const authorName = $(authorElement).text().trim();
			authors.push(authorName);
		});

		const ratingElement = $('.manga-info-text .manga-info-text-i span');
		const genresElement = $('.manga-info-text .manga-info-text-i a');

		const chapterElements = $('.chapter-name');
		const data = chapterElements
			.map((index, element) => {
				const src = $(element).attr('href');
				const chapterId = src ? src.split('/').slice(-1)[0] : null;

				return {
					src,
					chapterId,
					chapterTitle: $(element).text()
				};
			})
			.get();

		return new Response(
			JSON.stringify({
				episodes: data,
				title: titleElement.text(),
				img: imgElement.attr('src'),
				description: descriptionElement.text(),
				author: authors,
				rating: ratingElement.text(),
				genres: genresElement.text(),
				lastUpdated: lastUpated,
				views: viewCount
			})
		);
	} catch (error: any) {
		return new Response(
			JSON.stringify({
				episodes: error.message,
				failure: error
			})
		);
	}
};
