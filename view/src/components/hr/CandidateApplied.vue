<template>
	<div class="grid grid-cols-4 items-center">
		<div class="flex gap-2 items-center">
			<img
				src="https://themezhub.net/jobstock-landing-2.2/jobstock/assets/img/l-1.png"
				alt="company logo"
				class="w-12 h-12"
			/>
			<span>
				<h1
					class="text-sm md:text-base lg:text-lg text-sky-900 font-semibold hover:cursor-pointer"
				>
					{{ name }}
				</h1>
				<p class="text-xs lg:text-sm text-slate-500">
					{{ position }}
				</p>    
			</span>
		</div>

		<p class="text-xs md:text-sm lg:text-base text-slate-500">
			Ứng tuyển vào {{ time }}
		</p>

		<span
			class="p-2 bg-green-700 rounded-lg text-white w-20 md:w-24 text-xs md:text-sm lg:text-base text-center mx-auto"
			v-if="status === 'Chấp nhận'"
			>{{ status }}</span
		>
		<span
			class="p-2 bg-yellow-400 rounded-lg text-white w-20 md:w-24 text-xs md:text-sm lg:text-base text-center mx-auto"
			v-else-if="status === 'Đang chờ'"
			>{{ status }}</span
		>
		<span
			class="p-2 bg-red-500 rounded-lg text-white w-20 md:w-24 text-xs md:text-sm lg:text-base text-center mx-auto"
			v-else-if="status === 'Từ chối'"
			>{{ status }}</span
		>

		<font-awesome-icon
			icon="fa-solid fa-eye"
			class="p-2 bg-blue-100 text-blue-500 rounded-full text-sm md:text-base lg:text-lg hover:cursor-pointer mx-auto"
		/>
	</div>
</template>

<script lang="ts">
export default {
	props: {
		name: {
			type: String,
			required: true,
		},
		position: {
			type: String,
			required: true,
		},
		time: {
			type: String,
			required: true,
		},
		status: {
			type: String,
			required: true,
		},
		logo: {
			type: String,
			required: true,
		},
		id: {
			type: Number,
			required: true,
		},
	},
};
</script>
