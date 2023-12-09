<template>
	<div
		class="p-4 border border-slate-400 rounded-lg flex justify-between items-center"
	>
		<div class="flex gap-2 items-center">
			<img :src="logo" alt="job logo" class="w-12 h-12 lg:w-16 lg:h-16" />
			<span class="flex flex-col items-start justify-center">
				<router-link
					:to="candidateLink"
					class="text-xs md:text-sm lg:text-base font-semibold text-sky-900 hover:cursor-pointer hover:text-green-700"
					v-if="type === 'candidate'"
				>
					{{ name }}
				</router-link>
				<router-link
					:to="jobLink"
					class="text-xs md:text-sm lg:text-base font-semibold text-sky-900 hover:cursor-pointer hover:text-green-700"
					v-else
				>
					{{ name }}
				</router-link>
				<p
					class="flex items-center text-slate-600 text-xs lg:text-sm"
					v-if="type === 'job'"
				>
					<font-awesome-icon
						icon="fa-solid fa-location-dot"
						class="mr-1"
					/>{{ location }}
				</p>
				<p
					class="flex items-center text-slate-600 text-xs lg:text-sm"
					v-else
				>
					{{ position }}
				</p>
			</span>
		</div>

		<div class="flex items-center gap-4">
			<button
				class="px-2 py-1 lg:px-4 lg:py-2 border rounded-md border-slate-400 text-sky-900 hover:bg-slate-200 text-xs md:text-sm lg:text-base"
				v-if="type === 'job'"
			>
				{{ status }}
			</button>
			<select
				class="px-2 py-1 lg:px-4 lg:py-2 border rounded-md border-slate-400 text-sky-900 hover:bg-slate-200 text-xs md:text-sm lg:text-base"
                v-model="status"
				v-else
			>
				<option value="Đang chờ">Đang chờ</option>
				<option value="Chấp nhận">Chấp nhận</option>
				<option value="Từ chối">Từ chối</option>
			</select>
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
		position: {
			type: String,
			required: false,
		},
		status: {
			type: String,
			required: false,
		},
		id: {
			type: Number,
			required: false,
		},
		type: {
			type: String,
			default: "job",
		},
	},
    data() {
        return {
            status: this.status,
        }
    },
	computed: {
		jobLink() {
			return `/jobdetail/${this.id}`;
		},
		candidateLink() {
			return `/candidate/${this.id}/profile`;
		},
	},
};
</script>
