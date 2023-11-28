<template>
	<section class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Cập nhật thông tin công ty
		</h1>
		<form @submit.prevent="" class="bg-white p-4 rounded-lg">
			<div class="grid grid-cols-2 justify-center gap-4">
				<div class="flex flex-col text-sm text-gray-700 gap-1">
					<label for="logo" id="logo">Logo</label>
					<input
						type="file"
						@change="previewImage"
						id="logo"
						ref="fileInput"
					/>
					<div
						v-if="imagePreview"
						class="flex justify-center items-center gap-4"
					>
						<img
							:src="imagePreview"
							alt="Image preview"
							class="w-28 h-28 rounded-full mt-1 self-center border-2"
						/>
						<button
							class="w-6 h-6 flex items-center justify-center text-white rounded-full bg-red-500"
							@click="deleteImage"
						>
							X
						</button>
					</div>
				</div>
				<div>
					<label for="name" class="text-sm text-gray-700"
						>Tên công ty</label
					>
					<input
						type="text"
						name="name"
						id="name"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Tên công ty"
						value="Công ty ABC"
					/>
				</div>
				<div>
					<label for="address" class="text-sm text-gray-700"
						>Địa chỉ</label
					>
					<input
						type="text"
						name="address"
						id="address"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Địa chỉ"
						value="Cầu Giấy, Hà Nội"
					/>
				</div>
				<div>
					<label for="dob" class="text-sm text-gray-700"
						>Năm thành lập</label
					>
					<input
						type="text"
						name="dob"
						id="dob"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Năm thành lập"
						value="1990"
					/>
				</div>
				<div>
					<label for="emp_quantity" class="text-sm text-gray-700"
						>Số lượng nhân viên</label
					>
					<input
						type="text"
						name="emp_quantity"
						id="emp_quantity"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Số lượng nhân viên"
						value="10000+"
					/>
				</div>
				<div>
					<label for="contact" class="text-sm text-gray-700"
						>Liên lạc</label
					>
					<input
						type="text"
						name="contact"
						id="contact"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Liên lạc"
						value="sun@gmail.com"
					/>
				</div>
			</div>
			<button
				class="mt-4 py-2 px-6 bg-green-500 rounded-xl text-white hover:bg-green-600"
			>
				Xác nhận
			</button>
		</form>
	</section>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
	data() {
		return {
			imagePreview: null as string | null,
		};
	},
	methods: {
		previewImage(event: Event) {
			const file = (event.target as HTMLInputElement).files?.[0];
			if (file) {
				const reader = new FileReader();
				reader.onload = (e) => {
					this.imagePreview = e.target?.result as string | null;
				};
				reader.readAsDataURL(file);
			}
		},
		deleteImage() {
			this.imagePreview = null;
			(this.$refs.fileInput as HTMLInputElement).value = "";
		},
	},
});
</script>
