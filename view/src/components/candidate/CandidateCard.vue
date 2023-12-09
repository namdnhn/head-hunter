<template>
	<router-link :to="profileLink"
		class="border border-sky-800 hover:border-green-600 h-auto rounded-lg bg-white flex flex-col items-center gap-4 py-4"
	>
		<img :src="avt" alt="candidate avt" class="h-24 w-24 rounded-full" />
		<span class="flex flex-col items-center">
			<h1
				class="text-sm md:text-base lg:text-lg xl:text-xl text-sky-900 hover:cursor-pointer hover:text-green-600"
			>
				{{ name }}
			</h1>
			<p class="text-xs md:text-sm lg:text-base text-slate-500">
				{{ job }}
			</p>
			<p class="text-xs md:text-sm lg:text-base text-slate-500">
				{{ location }}
			</p>
		</span>
	</router-link>
</template>

<script lang="ts">
export default {
	props: {
		id: {
			type: Number,
			required: true,
		},
		avt: {
			type: String,
			required: true,
		},
		location: {
			type: String,
			required: true,
		},
		job: {
			type: String,
			required: true,
		},
		name: {
			type: String,
			required: true,
		},
	},
    computed: {
        profileLink(): string {
            return `/candidate/${this.id}/profile`;
        },
    },
};
</script>
