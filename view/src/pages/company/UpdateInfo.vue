<template>
	<section class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10">
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Cập nhật thông tin công ty
		</h1>
		<form @submit.prevent="" class="bg-white p-4 rounded-lg">
			<div class="grid grid-cols-2 justify-center gap-4">
				<div class="flex flex-col text-sm text-gray-700 gap-1">
					<label for="logo" id="logo">Logo</label>

					<img
						:src="company_info.logo"
						v-if="company_info.logo && !imagePreview"
						class="h-40 w-40"
					/>

					<div
						v-if="
							uploadedImage && !imagePreview && !company_info.logo
						"
						class=""
					>
						<img
							:src="uploadedImage"
							alt="logo"
							class="h-40 w-40"
						/>
					</div>

					<div>
						<input
							type="file"
							@change="previewImage"
							id="logo"
							ref="fileInput"
						/>
						<div
							v-if="imagePreview"
							class="flex items-center gap-4"
						>
							<img
								:src="imagePreview"
								alt="Image preview"
								class="mt-1 self-center border-2 max-h-48"
							/>
							<button
								class="w-6 h-6 flex items-center justify-center text-white rounded-full bg-red-500"
								@click="deleteImage"
							>
								X
							</button>
						</div>
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
						v-model="company_info.name"
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
						v-model="company_info.address"
					/>
				</div>
				<div>
					<label for="dob" class="text-sm text-gray-700"
						>Năm thành lập</label
					>
					<input
						type="number"
						name="dob"
						id="dob"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Năm thành lập"
						v-model="company_info.founded_year"
					/>
				</div>
				<div>
					<label for="emp_quantity" class="text-sm text-gray-700"
						>Số lượng nhân viên</label
					>
					<input
						type="number"
						name="emp_quantity"
						id="emp_quantity"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="Số lượng nhân viên"
						v-model="company_info.employee_quantity"
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
						v-model="company_info.contact"
					/>
				</div>

				<div class="col-span-2 flex gap-4">
					<label for="description" class="text-sm text-gray-700"
						>Giới thiệu công ty</label
					>

					<textarea
						rows="10"
						cols="80"
						class="px-2 py-1 border-2 border-black rounded"
						id="description"
						v-model="company_info.description"
					></textarea>
				</div>
			</div>
			<span
				class="mt-8 py-2 px-6 bg-green-500 rounded-xl text-white hover:bg-green-600"
				@click="submit"
			>
				Xác nhận
			</span>
		</form>
		<base-spinner v-if="isLoading"></base-spinner>
	</section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
	getStorage,
	ref,
	uploadBytesResumable,
	getDownloadURL,
} from "firebase/storage";
import {app} from "../../../services/app"; 

export default defineComponent({
	data() {
		return {
			imagePreview: null as string | null,
			imageFile: null as File | null,
			uploadedImage: null as string | null,
			company_info: {
				address: "",
				contact: "",
				description: "",
				employee_quantity: 0,
				founded_year: 0,
				id: 0,
				job_quantity: 0,
				logo: "",
				name: "",
				user_id: 0,
			},
			isLoading: false,
		};
	},
	methods: {
		previewImage(event: Event) {
			const file = (event.target as HTMLInputElement).files?.[0];
			if (file) {
				this.imageFile = file;
				const reader = new FileReader();
				reader.onload = (e) => {
					this.imagePreview = e.target?.result as string | null;
				};
				reader.readAsDataURL(file);
			}
		},
		deleteImage() {
			this.imagePreview = null;
			this.imageFile = null;
			(this.$refs.fileInput as HTMLInputElement).value = "";
		},
		async uploadImage() {
			if (this.imageFile) {
				this.isLoading = true;
				const storage = getStorage(app);
				const storageRef = ref(
					storage,
					"images/" + this.imageFile.name
				);

				const uploadTask = uploadBytesResumable(
					storageRef,
					this.imageFile
				);

				const uploadPromise = new Promise((resolve, reject) => {
					uploadTask.on(
						"state_changed",
						(snapshot) => {
							const progress =
								(snapshot.bytesTransferred /
									snapshot.totalBytes) *
								100;
							console.log("Upload is " + progress + "% done");
						},
						(error) => {
							console.error("Upload failed:", error);
							reject(error);
						},
						() => {
							getDownloadURL(uploadTask.snapshot.ref).then(
								(downloadURL) => {
									console.log(
										"File available at",
										downloadURL
									);
									this.uploadedImage = downloadURL;
									this.company_info.logo = downloadURL;
									resolve(downloadURL);
								}
							);
						}
					);
				});

				try {
					await uploadPromise;
				} catch (error) {
					console.error("Upload failed:", error);
				} finally {
					this.isLoading = false;
					this.deleteImage();
				}
			}
		},
		async getCompanyInfo() {
			const companyId = localStorage.getItem("companyId");
			try {
                this.isLoading = true;
				const res = await fetch(
					`http://localhost:8000/api/company/${companyId}`,
					{
						method: "GET",
						headers: {
							"Content-Type": "application/json",
						},
					}
				);

				const responseData = await res.json();
				this.company_info = responseData;
			} catch (error) {
				console.log(error);
			}
            this.isLoading = false;
		},
		async submit() {
			await this.uploadImage();
			this.imagePreview = null;
			this.imageFile = null;
			this.uploadedImage = null;

			try {
				this.isLoading = true;
				const res = await fetch(
					`http://localhost:8000/api/company/${this.company_info.id}`,
					{
						method: "PUT",
						headers: {
							"Content-Type": "application/json",
						},
						body: JSON.stringify(this.company_info),
					}
				);

				const responseData = await res.json();

				console.log(responseData);
			} catch (error) {
				console.log(error);
			}
			this.isLoading = false;
		},
	},
	mounted() {
		this.getCompanyInfo();
	},
});
</script>
