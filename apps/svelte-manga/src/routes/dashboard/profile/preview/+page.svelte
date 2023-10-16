<script>
	import Chat from '$lib/components/Chat.svelte';
	import { authData } from '$lib/utils/stores';
	import { pb } from '$lib/utils/api';

	const avatar = pb.authStore.model?.avatar
		? `${import.meta.env.VITE_PB_API_2}/api/files/_pb_users_auth_/${pb.authStore.model?.id}/${
				pb.authStore.model?.avatar
		  }`
		: `https://avatars.dicebear.com/api/adventurer-neutral/${pb.authStore.model?.username}.svg`;
</script>

<div class=" w-full">
	<main
		class="profile-page"
		style="background-image: url(https://images.unsplash.com/photo-1499336315816-097655dcfbda?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2710&q=80);"
	>
		<section class="relative block h-400-px">
			<div
				class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
				style="transform: translateZ(0);"
			>
				<svg
					class="absolute bottom-0 overflow-hidden"
					xmlns="http://www.w3.org/2000/svg"
					preserveAspectRatio="none"
					version="1.1"
					viewBox="0 0 2560 100"
					x="0"
					y="0"
				>
					<polygon class="text-blueGray-200 fill-current" points="2560 0 2560 100 0 100" />
				</svg>
			</div>
		</section>
		<section class="relative py-8 bg-blueGray-200">
			<div class="container mx-auto px-4">
				<div class="relative bg-base-100 w-full mb-6 shadow-xl rounded-lg">
					<div class="px-6 py-4">
						<div class="flex items-center justify-between">
							<img alt="Profile Avatar" src={avatar} class="rounded-full h-20 w-20 object-cover" />
							<button class="btn btn-outline btn-accent">Like</button>
						</div>
						<div class="text-center mt-6">
							<h3 class="text-2xl font-semibold text-blueGray-700">
								{$authData.username}
							</h3>
							<div class="text-sm text-blueGray-400 mt-2">
								<i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400" />
								{$authData.address}
							</div>
							<div class="text-sm text-blueGray-600 mt-1">
								<i class="fas fa-briefcase mr-2 text-lg text-blueGray-400" />
								{$authData.title}
							</div>
						</div>
						<div class="mt-6 text-center">
							<p class="text-lg leading-relaxed text-blueGray-700">
								{$authData.about}
							</p>
							<a href="#pablo" on:click={(e) => e.preventDefault()} class="text-red-500 font-bold"
								>Show more</a
							>
						</div>
					</div>
				</div>
			</div>
		</section>
	</main>
	<Chat />
</div>
