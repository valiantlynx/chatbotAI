<script lang="ts">
	import ChatMessage from './ChatMessage.svelte';
	import { onMount, onDestroy } from 'svelte';
	import { authData } from '$lib/utils/stores';
	import { pb } from '$lib/utils/api';
	import { page } from '$app/stores';

	let newMessage: string;
	let messages: any[] = [];
	let unsubscribe: () => void;
	let scrollBottom: HTMLDivElement;
	let lastScrollTop: number;
	let canAutoScroll = true;
	let unreadMessages = false;

	function autoScroll() {
		setTimeout(() => scrollBottom?.scrollIntoView({ behavior: 'smooth' }), 50);
		unreadMessages = false;
	}

	function watchScroll(e: any) {
		canAutoScroll = (e.target.scrollTop || Infinity) > lastScrollTop;
		lastScrollTop = e.target.scrollTop;
		unreadMessages = !canAutoScroll;
	}

	async function getInitialMessages() {
		try {
			const resultList = await pb.collection('chat_animevariant').getList(1, 50, {
				sort: 'created',
				filter: $page.params.chapterid
					? `mangaid="${$page.params.id}"&&chapterid="${$page.params.chapterid}"`
					: `mangaid="${$page.params.id}"`,
				expand: 'sender'
			});

			return resultList.items;
		} catch (error) {
			console.error('Fetching initial messages error:', error);
			return [];
		}
	}

	async function handleRealtimeMessage({ action, record }: any) {
		try {
			if (action === 'create') {
				const sender = await pb.collection('users').getOne(record.sender);
				record.expand = { sender };
				messages = [...messages, record];

				if ($authData.id !== record.receiver) {
					unreadMessages = true;
				}
			}
			if (action === 'delete') {
				messages = messages.filter((m) => m.id !== record.id);
			}
		} catch (error) {
			console.error('Realtime message subscription error:', error);
		}
	}

	onMount(async () => {
		messages = await getInitialMessages();
		unsubscribe = await pb.collection('chat_animevariant').subscribe('*', handleRealtimeMessage);
	});

	onDestroy(() => {
		unsubscribe?.();
	});

	async function sendMessage() {
		const data = {
			message: newMessage,
			sender: pb.authStore.model?.id,
			chapterid: $page.params.chapterid,
			mangaid: $page.params.id,
			receiver: pb.authStore.model?.id
		};
		await pb.collection('chat_animevariant').create(data);
		newMessage = '';
		canAutoScroll = true;
		autoScroll();
	}
</script>

<div class="container p-4 space-y-4">
	<h2 class="text-2xl font-bold mb-4">Join the Discussion</h2>

	<main class="overflow-y-auto max-h-[60vh]" on:scroll={watchScroll}>
		{#each messages as message (message.id)}
			<ChatMessage {message} sender={$authData.username} />
		{/each}
		<div class="dummy" bind:this={scrollBottom} />
	</main>

	{#if !canAutoScroll}
		<div class="text-center justify-center flex">
			<button on:click={autoScroll} class="btn btn-primary">
				{#if unreadMessages}
					💬
				{/if}
				🡣
			</button>
		</div>
	{/if}

	<div class="border-t border-primary pt-4">
		<form on:submit|preventDefault={sendMessage} class="space-x-2 flex items-center">
			<input
				type="text"
				placeholder={pb.authStore.isValid ? 'Type a message...' : 'Login to chat... ------>'}
				bind:value={newMessage}
				maxlength="100"
				class="input input-bordered input-primary flex-grow animate-pulse"
			/>
			{#if pb.authStore.isValid}
				<button type="submit" disabled={!newMessage} class="btn btn-primary"> Send </button>
			{:else}
				<a href="/login" type="submit" class="btn btn-primary"> Login </a>
			{/if}
		</form>
	</div>
</div>
