<template>
	<span class="flex items-center gap-2" v-if="type === 'received'">
		<img
			:src="avt"
			alt="avt"
			class="h-8 w-8 rounded-full"
		/>
		<p class="px-2 py-1 rounded-3xl bg-slate-200" :title="time">{{ content }}</p>
	</span>

	<span class="flex items-center gap-2 self-end" v-else-if="type === 'sent'">
		<p class="px-2 py-1 rounded-3xl bg-slate-200" :title="time">{{ content }}</p>
		<img
			:src="avt"
			alt="avt"
			class="h-8 w-8 rounded-full"
		/>
	</span>
</template>

<script lang="ts">
export default {
	props: {
		type: {
			type: String,
			required: true,
		},
		avt: {
			type: String,
			required: false,
		},
		content: {
			type: String,
			required: true,
		},
		time: {
			type: String,
			required: true,
		},
	},
};
</script>
