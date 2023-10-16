<script lang="ts">
	import { browser, dev } from '$app/environment';
	import { theme } from '$lib/config/general';
	import { hslToHex } from '$lib/utils/color';
	import Icon from '@iconify/svelte';

	let currentTheme: string;
	let currentThemeColor: string;
	let pin = true;
	let percent: number;
	let [scrollY, lastY] = [0, 0];

	$: if (browser && currentTheme) {
		document.documentElement.setAttribute('data-theme', currentTheme);
		// eslint-disable-next-line @typescript-eslint/no-unused-vars
		currentThemeColor = hslToHex(
			...(getComputedStyle(document.documentElement)
				.getPropertyValue('--b1')
				.slice(dev ? 1 : 0)
				.replaceAll('%', '')
				.split(' ')
				.map(Number) as [number, number, number])
		);
	}

	$: if (scrollY) {
		pin = lastY - scrollY > 0 || scrollY === 0 ? true : false;
		lastY = scrollY;
		if (browser)
			// eslint-disable-next-line @typescript-eslint/no-unused-vars
			percent =
				Math.round(
					(scrollY /
						(document.documentElement.scrollHeight - document.documentElement.clientHeight)) *
						10000
				) / 100;
	}

	if (browser)
		currentTheme =
			localStorage.getItem('theme') ??
			(window.matchMedia('(prefers-color-scheme: dark)').matches
				? theme?.[1].name
				: theme[0].name ?? theme[0].name);
</script>

<div id="change-theme" class="dropdown dropdown-end">
	<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
	<!-- reference: https://github.com/saadeghi/daisyui/issues/1285 -->
	<div tabindex="0" class="btn btn-circle btn-ghost">
		<Icon icon="heroicons-outline:color-swatch" width="30" />
	</div>

	<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
	<!-- reference: https://github.com/saadeghi/daisyui/issues/1285 -->
	<ul
		tabindex="0"
		class="flex z-[1] flex-nowrap shadow-2xl menu dropdown-content bg-base-100 text-base-content rounded-box w-52 p-2 gap-2 overflow-y-auto max-h-[21.5rem]"
		class:hidden={!pin}
	>
		{#each theme as { name, text }}
			<button
				data-theme={name}
				on:click={() => {
					currentTheme = name;
					localStorage.setItem('theme', name);
				}}
				class:border-2={currentTheme === name}
				class:border-primary={currentTheme === name}
				class="btn btn-ghost w-full hover:bg-primary group rounded-lg flex bg-base-100 p-2 transition-all"
			>
				<p
					class="flex-1 text-left text-base-content group-hover:text-primary-content transition-color"
				>
					{text ?? name}
				</p>
				<div class="grid grid-cols-4 gap-0.5 m-auto">
					{#each ['bg-primary', 'bg-secondary', 'bg-accent', 'bg-neutral'] as bg}
						<div class={`${bg} w-1 h-4 rounded-btn`} />
					{/each}
				</div>
			</button>
		{/each}
	</ul>
</div>
