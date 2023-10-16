
import { site } from './site';

export const favicon = {
	src: site.protocol + site.domain + '/favicon.png',
	sizes: '48x48',
	type: 'image/png'
};

export const any = {
	180: {
		src: site.protocol + site.domain + '/assets/any@180.png',
		sizes: '180x180',
		type: 'image/png'
	},
	192: {
		src: site.protocol + site.domain + '/assets/any@192.png',
		sizes: '192x192',
		type: 'image/png'
	},
	512: {
		src: site.protocol + site.domain + '/assets/any@512.png',
		sizes: '512x512',
		type: 'image/png'
	}
};

export const maskable = {
	192: {
		src: site.protocol + site.domain + '/assets/maskable@192.png',
		sizes: '192x192',
		type: 'image/png'
	},
	512: {
		src: site.protocol + site.domain + '/assets/maskable@512.png',
		sizes: '512x512',
		type: 'image/png'
	}
};
