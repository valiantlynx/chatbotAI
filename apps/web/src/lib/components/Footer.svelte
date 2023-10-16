<script>
	import { site } from '$lib/config/site';
	import Icon from '@iconify/svelte';
</script>

<footer class="footer footer-center p-10 bg-base-300 text-base-content rounded mt-auto">
	<div class="grid grid-flow-col gap-4">
		<a href="/about" class="link link-hover">About us</a>
		<a href="/contact" class="link link-hover">Contact</a>
		<a href="/privacy-policy" class="link link-hover">Privacy</a>
	</div>
	<div>
		<div class="grid grid-flow-col gap-4">
			<a href="https://www.facebook.com/animevariant/" class="link link-hover hover:link-primary"
				><Icon icon="mdi:twitter" /></a
			>
			<a href="https://www.youtube.com/@valiantlynx/" class="link link-hover hover:link-primary"
				><Icon icon="mdi:youtube" /></a
			>
			<a href="https://www.facebook.com/animevariant/" class="link link-hover hover:link-primary"
				><Icon icon="mdi:facebook" /></a
			>
		</div>
	</div>
	<div>
		<p>Copyright © 2023 - All right reserved by {site.company}</p>
	</div>
</footer>
