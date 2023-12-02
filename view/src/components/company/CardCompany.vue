<template>
	<li
		class="bg-slate-50 border border-sky-800 hover:border-green-600 h-auto rounded-lg grid grid-rows-2 items-center justify-center py-10"
	>
		<!-- job desc  -->
		<span class="w-full flex items-center justify-center">
		    <img
    			:src="logo"
    			alt="logo company"
    			class="w-20 h-auto hover:cursor-pointer"
    		/>
		</span>
		<div class="text-center mt-4 flex flex-col">
			<router-link
				:to="companyDetaliLink"
				class="text-sky-900 font-bold text-sm md:text-base lg:text-xl hover:cursor-pointer hover:text-green-700"
				>{{ name }}</router-link
			>
			<span class="text-gray-500 text-xs md:text-sm lg:text-base">
				<font-awesome-icon :icon="['fas', 'location-dot']" />
				{{ address }}
			</span>
		</div>
	</li>
</template>

<script lang="ts">
export default {
	props: {
		id: {
			type: String,
			required: true,
		},
		logo: {
			type: String,
			required: true,
		},
		name: {
			type: String,
			required: true,
		},
		address: {
			type: String,
			required: true,
		},
	},
	computed: {
		companyDetaliLink() {
			return "/companyprofile/" + this.id;
		},
	},
};
</script>
