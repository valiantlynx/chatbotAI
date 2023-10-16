/**
 * @file General configuration file
 * @module general-config/general
 * @typedef {Object} any
 * 
 */
export const API_BASE_URL = 'https://api.texbab.com';

export const theme = [
	{
		name: 'halloween',
		text: '🎃 Halloween'
	},
	{
		name: 'dracula',
		text: '🧛 Dracula'
	},
	{
		name: 'cyberpunk',
		text: '🤖 Cyberpunk'
	},
	{
		name: 'business',
		text: '🏢 Business'
	},
	{
		name: 'lofi',
		text: '🎶 Lo-Fi'
	},
	{
		name: 'coffee',
		text: '☕ Coffee'
	},
	{
		name: 'forest',
		text: '🌳 Forest'
	},
	{
		name: 'wireframe',
		text: '📏 Wireframe'
	},
	{
		name: 'night',
		text: '🌃 Night'
	},
	{
		name: 'retro',
		text: '🌇 Retro'
	},
	{
		name: 'winter',
		text: '🌨️ Winter'
	},
	{
		name: 'bumblebee',
		text: '🐝 Bumblebee'
	},
	{
		name: 'light',
		text: '🌞 Light'
	},
	{
		name: 'dark',
		text: '🌑 Dark'
	},
	{
		name: 'cupcake',
		text: '🧁 Cupcake'
	},
	{
		name: 'emerald',
		text: '💎 Emerald'
	},
	{
		name: 'corporate',
		text: '🏢 Corporate'
	},
	{
		name: 'synthwave',
		text: '🌃 Synthwave'
	},
	{
		name: 'valentine',
		text: '🌸 Valentine'
	},
	{
		name: 'garden',
		text: '🏡 Garden'
	},
	{
		name: 'aqua',
		text: '💦 Aqua'
	},
	{
		name: 'pastel',
		text: '🎨 Pastel'
	},
	{
		name: 'fantasy',
		text: '🧚 Fantasy'
	},

	{
		name: 'black',
		text: '🖤 Black'
	},
	{
		name: 'luxury',
		text: '💎 Luxury'
	},
	{
		name: 'cmyk',
		text: '🖨 CMYK'
	},
	{
		name: 'autumn',
		text: '🍂 Autumn'
	},

	{
		name: 'acid',
		text: '💊 Acid'
	},
	{
		name: 'lemonade',
		text: '🍋 Lemonade'
	}
];

export const menu = [
	{
		img: `${API_BASE_URL}/api/files/eijp9z2zxlgrd4a/rzx50a9wq8sjf5q/0d537318c00611ec84202eb08599686b_a5987812_7e71_11eb_99f8_ea53df50c496_5cc54b47842a7094ebaec2aef0611d_p4L4GTD1XO.png`,
		title: 'Barne',
		slug: '/menu/texbab_barnemenu'
	},
	{
		img: `${API_BASE_URL}/api/files/eijp9z2zxlgrd4a/rzx50a9wq8sjf5q/0d537318c00611ec84202eb08599686b_a5987812_7e71_11eb_99f8_ea53df50c496_5cc54b47842a7094ebaec2aef0611d_p4L4GTD1XO.png`,
		title: 'Burger',
		slug: '/menu/texbab_burger'
	},
	{
		img: `${API_BASE_URL}/api/files/qlhqb7ir7o548t1/mkimb7hoxx1oz9i/main_header_WouOltkLLE.webp`,
		title: 'Eat Green',
		slug: '/menu/texbab_eat_green'
	},
	{
		img: `${API_BASE_URL}/api/files/0zali0zpl9bb4yh/kvdj8zevopzn45m/download_1_GHHWWEdu1g.jpeg`,
		title: 'Kebab',
		slug: '/menu/texbab_kebab'
	},
	{
		img: `${API_BASE_URL}/api/files/latdufbxmqnxcrk/77v7kftyfnw4b2z/pizza_Lqbuwn5M31.jpg`,
		title: 'Pizza',
		slug: '/menu/texbab_pizza'
	},
	{
		img: `${API_BASE_URL}/api/files/izawv6hmhwokkqa/nv0fft46f7g54kg/badge_2_bg_2b4OkbBwRK.png`,
		title: 'smaretter',
		slug: '/menu/texbab_smaretter'
	},
	{
		img: `${API_BASE_URL}/api/files/eijp9z2zxlgrd4a/rzx50a9wq8sjf5q/0d537318c00611ec84202eb08599686b_a5987812_7e71_11eb_99f8_ea53df50c496_5cc54b47842a7094ebaec2aef0611d_p4L4GTD1XO.png`,
		title: 'Full',
		slug: '/menu/texbab_fullmenu'
	},
	{
		img: `${API_BASE_URL}/api/files/izawv6hmhwokkqa/nv0fft46f7g54kg/badge_2_bg_2b4OkbBwRK.png`,
		title: 'Special',
		slug: '/menu/texbab_special'
	}
];

// the icons are from https://iconify.design
export const badge = [
	{
		icon: 'mdi:child-toy',
		title: 'Barne',
		slug: '/menu/texbab_barnemenu'
	},
	{
		icon: 'majesticons:burger-line',
		title: 'Burger',
		slug: '/menu/texbab_burger'
	},
	{
		icon: 'raphael:green',
		title: 'Eat Green',
		slug: '/menu/texbab_eat_green'
	},
	{
		title: 'Kebab',
		icon: 'game-icons:kebab-spit',
		slug: '/menu/texbab_kebab'
	},
	{
		title: 'Pizza',
		slug: '/menu/texbab_pizza',
		icon: 'emojione-monotone:pizza'
	},
	{
		title: 'smaretter',
		slug: '/menu/texbab_smaretter',
		icon: 'map:food'
	},
	{
		title: 'Full',
		slug: '/menu/texbab_fullmenu',
		icon: 'arcticons:foodora-dk'
	},
	{
		title: 'Special',
		slug: '/menu/texbab_special',
		icon: 'emojione-monotone:face-savoring-food'
	}
];

export const header = {
	nav: [
		{
			text: 'About',
			link: '/about'
		},
		{
			text: 'Other Projects',
			link: '/projects'
		}
	]
};

export const footer = {
	nav: [
		{
			text: 'Feed',
			link: '/atom.xml'
		},
		{
			text: 'Sitemap',
			link: '/sitemap.xml'
		},
		{
			text: 'Minfuel',
			link: 'https://minfuel.no'
		},
		{
			text: 'Altlokalt',
			link: 'https://Altlokalt.com'
		},
		{
			text: 'Animevariant',
			link: 'https://Animevariant.com'
		}
	]
};

export const date = {
	locales: 'en-US',
	options: {
		year: '2-digit',
		weekday: 'long',
		month: 'short',
		day: 'numeric'
	}
};

export const feed = {};
