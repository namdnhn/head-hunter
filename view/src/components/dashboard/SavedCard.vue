<template>
	<div
		class="p-4 border border-slate-400 rounded-lg flex justify-between items-center"
	>
		<div class="flex gap-2 items-center">
			<img :src="logo" alt="job logo" class="w-12 h-12 lg:w-16 lg:h-16" />
			<span class="flex flex-col items-start justify-center">
				<h5
					class="text-xs md:text-sm lg:text-base font-semibold text-sky-900 hover:cursor-pointer hover:text-green-700"
				>
					{{ name }}
				</h5>
				<p class="flex items-center text-slate-600 text-xs lg:text-sm" v-if="type==='job'">
					<font-awesome-icon
						icon="fa-solid fa-location-dot"
						class="mr-1"
					/>{{ location }}
				</p>
                <p class="flex items-center text-slate-600 text-xs lg:text-sm" v-else>
                    {{ position }}
				</p>
			</span>
		</div>

		<p class="text-xs md:text-sm lg:text-base text-slate-500" v-if="expire">
			Hết hạn vào {{ expire }}
		</p>

		<div class="flex items-center gap-4">
			<font-awesome-icon
				icon="fa-solid fa-xmark"
				class="py-1 px-2 text-white bg-red-500 hover:cursor-pointer rounded-full text-xs md:text-sm lg:text-base"
			/>
			<button
				class="px-2 py-1 lg:px-4 lg:py-2 border rounded-md border-slate-400 text-sky-900 hover:bg-slate-200 text-xs md:text-sm lg:text-base"
			>
				Xem chi tiết
			</button>
			<button
				class="px-2 py-1 lg:px-4 lg:py-2 rounded-md border bg-green-300 text-sky-900 hover:bg-green-400 text-xs md:text-sm lg:text-base"
				v-if="type === 'job'"
			>
				Ứng tuyển nhanh
			</button>
		</div>
	</div>
</template>

<script lang="ts">
export default {
	props: {
		logo: {
			type: String,
			required: true,
		},
		name: {
			type: String,
			required: true,
		},
		location: {
			type: String,
			required: false,
		},
		expire: {
			type: String,
			required: false,
		},
		type: {
			type: String,
			required: false,
		},
        position: {
            type: String,
            required: false
        }
	},
};
</script>
