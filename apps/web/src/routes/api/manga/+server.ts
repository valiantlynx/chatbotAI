import type { RequestHandler } from './$types';
import axios from 'axios';
import cheerio from 'cheerio';

export const GET: RequestHandler = async ({ url }) => {
	const page = url.searchParams.get('page');

	// Your logic for handling the page parameter and generating the response
	const headers = {
		'Access-Control-Allow-Origin': '*',
		'Content-Type': 'application/json'
	};

	try {
		const apiUrl = `${import.meta.env.VITE_IMAGE_URL}/genre/Isekai?type=topview&page=${page}`;

		const response: any = await axios
			.get(apiUrl, {
				headers: {
					'Access-Control-Allow-Origin': '*',
					'Content-Type': 'application/json'
				}
			})
			.catch((err: any) => {
				console.error(
					'error: ',
					err.message,
					err.response,
					err.response.data,
					err.data,
					err.status
				);
			});
		const $ = cheerio.load(response.data);

		const scrapedData: any = [];

		$('.content-genres-item').each((index: any, element: any) => {
			const titleElement = $(element).find('.genres-item-name');
			const imgElement = $(element).find('img');
			const chaptersElement = $(element).find('.genres-item-chap');
			const srcElement = $(element).find('a');
			const descriptionElement = $(element).find('.genres-item-description');
			const authorElement = $(element).find('.genres-item-author');
			const ratingElement = $(element).find('.genres-item-rate');

			// Extract the ID and title ID from the src URL
			const src = srcElement.attr('href');
			const id = src ? src.split('/').slice(-1)[0] : null;
			const titleId = titleElement.text();

			const content = {
				title: titleElement.text(),
				img: imgElement.attr('src'),
				latestChapter: chaptersElement.text(),
				rating: ratingElement.text(),
				src,
				id,
				titleId,
				description: descriptionElement.text(),
				author: authorElement.length
					? [authorElement.text(), authorElement.find('a').attr('href')]
					: null
			};
			scrapedData.push(content);
		});

		return new Response(
			JSON.stringify({
				page: page,
				mangas: scrapedData
			}),
			{ headers }
		);
	} catch (error: any) {
		return new Response(
			JSON.stringify({
				error: error.message,
				failure: error
			}),
			{ headers }
		);
	}
};
