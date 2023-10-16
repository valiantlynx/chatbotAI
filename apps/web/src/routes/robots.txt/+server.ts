import type { RequestHandler } from './$types';

const renderRobotsTxt = (url: string): string => {
	const robotsTxtContent = `User-agent: *
Allow: /
Sitemap: ${url}/sitemap.xml`;

	return robotsTxtContent;
};

export const trailingSlash = 'never';

export const GET: RequestHandler = async ({ url }) => {
	const robotsTxtContent = renderRobotsTxt(url.origin);
	return new Response(robotsTxtContent, {
		headers: {
			'content-type': 'text/txt; charset=utf-8'
		}
	});
};
