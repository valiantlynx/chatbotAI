<script lang="ts">
	// Import required modules
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import * as THREE from 'three';

	// Declare a variable to hold the container element
	let canvasContainer: any;

	// Check if the code is running in the browser environment
	if (browser) {
		// Declare variables for Three.js components
		let camera: THREE.PerspectiveCamera;
		let scene: THREE.Scene;
		let renderer: THREE.WebGLRenderer;
		let cube: THREE.Mesh<THREE.BoxGeometry, THREE.MeshBasicMaterial>;

		// Run this code when the component is mounted
		onMount(() => {
			// Create a Three.js scene, camera, and renderer
			scene = new THREE.Scene();
			camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000); // Aspect ratio set to 1 initially, the first parameter is the field of view, the second is the aspect ratio, the third is the near clipping plane, and the fourth is the far clipping plane
			renderer = new THREE.WebGLRenderer();

			// Calculate initial canvas size based on the container
			const canvasWidth = canvasContainer.clientWidth;
			const canvasHeight = canvasContainer.clientHeight;

			// Set renderer size and add Tailwind classes to make it responsive
			renderer.setSize(canvasWidth, canvasHeight);
			renderer.domElement.classList.add('w-full', 'h-full');

			// Append renderer's canvas to the container
			canvasContainer.appendChild(renderer.domElement);

			// Create a cube geometry and material, add it to the scene
			const geometry = new THREE.BoxGeometry(1, 1, 1);
			const material = new THREE.MeshBasicMaterial({ color: 0x66ccff }); // Blue color
			cube = new THREE.Mesh(geometry, material);
			scene.add(cube);

			// Set camera position
			camera.position.z = 5;

			// Start the animation loop
			animate();
		});

		// Function to render the scene
		const render = () => {
			renderer.clear();
			renderer.render(scene, camera);
		};

		// Animation loop
		const animate = () => {
			requestAnimationFrame(animate);

			// Rotate the cube
			cube.rotation.x += 0.05;
			cube.rotation.y += 0.05;

			// Update the camera's aspect ratio and position
			camera.aspect = canvasContainer.clientWidth / canvasContainer.clientHeight;
			camera.updateProjectionMatrix();

			// Render the scene
			render();
		};
	}
</script>

<svelte:head>
	<title>SvelteKit + Three.js</title>
</svelte:head>
<div class="flex flex-col items-center justify-center">
	<h1 class="text-3xl font-bold mb-6 text-center">SvelteKit + Three.js</h1>
	<p class="text-center">
		This is a demo of how to use Three.js with SvelteKit. The cube below is rendered using Three.js.
	</p>
	<section bind:this={canvasContainer} class="w-36 h-36 flex justify-center items-center">
		<!-- The canvas element will be appended here -->
	</section>
</div>
