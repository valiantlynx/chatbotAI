// stores.js
import { writable } from 'svelte/store';

// Initial cart state
const initialCart: any[] = [];

// Initial cart state
const initialUser: any = {};

// Create the cart store
export const cart = writable(initialCart);
export const order = writable(initialCart);

// Current User
export const authData = writable(initialUser);

const sidebarOpen = writable(true);

const toggleSidebar = () => {
	sidebarOpen.update((prev) => !prev);
};

const closeSidebar = () => {
	sidebarOpen.update(() => false);
};

export { sidebarOpen, toggleSidebar, closeSidebar };

// Current sidebar section
export const currentSection = writable('');

// Current page
export const currentPage = writable(1);

// pocketbase response
export const pocketbaseResponse = writable({
	page: 1,
	perPage: 5,
	totalItems: 0,
	totalPages: 0,
	items: []
});

// search query
export const searchQuery = writable('');

export const metaKeywords = writable('');

const log: any[] = [
	{
		log: 'log',
		time: new Date(),
		progress: 0,
		total: 0
	}
];

export const addedReadingProgress = writable(log);

const popularmanga: any[] = [{}];

export const popular: any = writable(popularmanga);

const latestmanga: any[] = [{}];

export const latest: any = writable(latestmanga);
