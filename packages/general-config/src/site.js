
export const site = {
	protocol: process.env.URARA_SITE_PROTOCOL ?? process.env.DEV ? 'http://' : 'https://',
	domain: process.env.VITE_SITE_URL ?? 'animevariant.com',
	logo: process.env.VITE_SITE_LOGO ?? '/logo.png',
	company: process.env.VITE_SITE_COMPANY ?? 'Valiantlynx',
	email: process.env.VITE_SITE_EMAIL ?? 'valiantlynxz@gmail.com',
	noImage: process.env.VITE_SITE_NO_IMAGE ?? '/assets/no-image.png',
	title: 'Animevariant',
	subtitle: 'Where Imagination Meets Innovation',
	pocketbase: process.env.VITE_PB_URL ?? 'https://nameless-cloud-5581.fly.dev',
	lang: 'en-US',
	description:
		'Read the latest manga online for free at animevariant.org, update fastest, most full, synthesized 24h free with high-quality images and be the first one to publish new chapters.',
	author: {
		avatar: '/assets/maskable@512.png',
		name: 'Valiantlynx',
		status: '🌸',
		bio: 'Multi-Disciplinary Engineer: Exploring the Intersection of AI, Blockchain, Web Development, and Product Design'
	},
	themeColor: '#3D4451'
};
