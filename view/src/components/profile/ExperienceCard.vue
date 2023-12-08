<template>
	<li class="flex justify-between items-center">
		<div class="flex items-center gap-2 lg:gap-4">
			<span class="flex flex-col">
				<h2
					class="text-xs md:text-sm lg:text-base text-sky-800 font-semibold"
					v-if="!isEditting"
				>
					{{ name }}
				</h2>
				<input
					type="text"
					class="text-xs md:text-sm lg:text-base px-2 py-1 mb-1 border border-sky-950 w-full"
					v-else
					:value="name"
					@input="
						$emit(
							'update:name',
							($event.target as HTMLInputElement).value
						)
					"
				/>

				<ul
					class="flex mt-1 md:mt-0 flex-col md:flex-row gap-2 lg:gap-4 text-xs lg:text-sm text-gray-500"
				>

					<li v-if="!isEditting">
						{{ duration }}
					</li>
					<input
						type="text"
						class="text-xs md:text-sm lg:text-base px-2 py-1 mb-1 border border-sky-950 text-black w-full" 
						v-else
						:value="duration"
						@input="
							$emit(
								'update:duration',
								($event.target as HTMLInputElement).value
							)
						"
					/>
				</ul>
			</span>
		</div>
		<font-awesome-icon
			icon="fa-solid fa-xmark"
			class="text-xs md:text-sm lg:text-base text-green-700 hover:cursor-pointer"
			@click="deleteExperience(id)"
			v-if="isEditting"
		/>
	</li>
</template>

<script lang="ts">
export default {
	emits: [
		"delete-experience",
		"update:name",
		"update:role",
		"update:duration",
	],
	props: {
		id: {
			type: Number,
			required: true,
		},
		name: {
			type: String,
			required: true,
		},
		time: {
			type: String,
			required: true,
		},
		duration: {
			type: String,
			required: true,
		},
		isEditting: {
			type: Boolean,
			default: false,
		},
	},
	methods: {
		deleteExperience(id: Number) {
			this.$emit("delete-experience", id);
		},
	},
};
</script>
