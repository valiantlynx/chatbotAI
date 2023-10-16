<script lang="ts">
	import Footer from '$lib/components/Footer.svelte';
	import Nav from '$lib/components/Nav.svelte';
	import '../app.css';
</script>

<Nav />
<slot />
<Footer />
