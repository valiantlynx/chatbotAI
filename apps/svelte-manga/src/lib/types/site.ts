import type { FFFAuthor } from 'fff-flavored-frontmatter';

export type SiteConfig = {
	/** site protocol. for example: `https://` */
	protocol: string;
	/** site domain. for example: `example.com` */
	domain: string;
	/** site title. */
	title: string;
	/** site subtitle. */
	subtitle?: string;
	/** site logo. `<link rel="icon" href={site.logo} />` */
	logo?: string;
	/** site lang. `<html lang={site.lang}>` */
	lang?: string;
	/** site pocketbase. `<meta name="pocketbase" content={site.pocketbase}>` */
	pocketbase?: string;
	/** site company. `<meta name="company" content={site.company}>` */
	company?: string;
	/** site email. `<meta name="email" content={site.email}>` */
	email?: string;
	/** site no-image. `<meta name="no-image" content={site.noImage}>` */
	noImage?: string;
	/** site description. `<meta name="description" content={site.description}>` */
	description?: string;
	/** site keywords. `<meta name="keywords" content={site.keywords}>` */
	keywords?: string[];
	author: Omit<FFFAuthor, 'url'> & {
		status?: string;
		bio?: string;
		metadata?: (
			| {
					text: string;
					icon?: string;
					link?: string;
					rel?: string;
			  }
			| {
					text?: string;
					icon: string;
					link?: string;
					rel?: string;
			  }
		)[];
	};
	/** for web app manifest only.
	 * ```
	 * "background_color": {site.themeColor},
	 * "theme_color": {site.themeColor}
	 * ```
	 */
	themeColor?: string;
};
