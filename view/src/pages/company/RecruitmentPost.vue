<template>
	<main class="py-32 px-40">
		<section class="border border-green-400 p-4 rounded">
			<h1
				class="text-base sm:text-lg md:text-xl lg:text-2xl text-sky-900 font-semibold mb-4"
			>
				Tạo tin tuyển dụng
			</h1>
			<form @submit.prevent="handleSubmit" class="grid grid-cols-2 gap-4">
				<div class="flex flex-col gap-1">
					<label for="role" class="max-w-fit"
						>Vị trí tuyển dụng</label
					>
					<input
						type="text"
						id="role"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="VD: Backend Developer"
						@input="role.errorMessage = ''"
                        v-model="role.value"
					/>
					<span
						class="text-xs lg:text-sm text-red-500"
						v-if="role.errorMessage"
						>{{ role.errorMessage }}</span
					>
				</div>

				<div class="flex flex-col gap-1">
					<label for="level" class="max-w-fit">Trình độ</label>
					<input
						type="text"
						id="level"
						placeholder="VD: Senior"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="level.errorMessage = ''"
                        v-model="level.value"
					/>
					<span
						class="text-xs lg:text-sm text-red-500"
						v-if="level.errorMessage"
						>{{ level.errorMessage }}</span
					>
				</div>

				<div class="flex flex-col gap-1">
					<label for="quantity" class="max-w-fit"
						>Số lượng tuyển dụng</label
					>
					<input
						type="text"
						id="quantity"
						placeholder="VD: 4"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="quantity.errorMessage = ''"
                        v-model="quantity.value"
					/>
					<span
						class="text-xs lg:text-sm text-red-500"
						v-if="quantity.errorMessage"
						>{{ quantity.errorMessage }}</span
					>
				</div>

				<div class="flex flex-col gap-1">
					<label for="address" class="max-w-fit"
						>Địa chỉ làm việc</label
					>
					<input
						type="text"
						id="address"
						placeholder="VD: Tầng 19, Leadvisors Tower, 643 Phạm Văn Đồng, Bắc Từ Liêm"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="address.errorMessage = ''"
                        v-model="address.value"
					/>
					<span
						class="text-xs lg:text-sm text-red-500"
						v-if="address.errorMessage"
						>{{ address.errorMessage }}</span
					>
				</div>

				<div class="flex flex-col gap-1">
					<div class="flex gap-4 items-center">
						<label for="skill" class="min-w-fit max-w-fit"
							>Kỹ năng yêu cầu</label
						>
						<ul
							class="flex items-end gap-2 overflow-auto"
							v-if="skills.value.length > 0"
						>
							<li
								class="px-2 py-1 border border-green-400 rounded-xl flex items-center gap-2"
								v-for="(skill, index) in skills.value"
							>
								{{ skill }}
								<font-awesome-icon
									icon="fa-solid fa-xmark"
									class="hover:cursor-pointer text-red-600"
									@click="deleteSkill(index)"
								/>
							</li>
						</ul>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="skills.errorMessage"
							>{{ skills.errorMessage }}</span
						>
					</div>
					<div class="flex items-center gap-4">
						<input
							type="text"
							id="skill"
							placeholder="VD: HTML, CSS"
							class="border border-gray-300 p-2 rounded-md w-full"
							v-model="newSkill"
							@input="skills.errorMessage = ''"
						/>
						<button
							class="px-2 py-1 bg-green-400 rounded-lg text-sky-900 hover:cursor-pointer"
							@click="addSkill"
							v-if="newSkill"
						>
							Thêm
						</button>
					</div>
				</div>

				<div class="flex flex-col gap-1">
					<label for="salary" class="max-w-fit">Mức lương</label>
					<input
						type="text"
						id="salary"
						placeholder="VD: 1k$ - 2k$"
						class="border border-gray-300 p-2 rounded-md w-full"
                        @input="salary.errorMessage = ''"
                        v-model="salary.value"
					/>
                    <span
                        class="text-xs lg:text-sm text-red-500"
                        v-if="salary.errorMessage"
                        >{{ salary.errorMessage }}</span>
				</div>

				<div class="flex flex-col gap-1">
					<label for="description" class="max-w-fit"
						>Mô tả công việc</label
					>
					<textarea
						name=""
						id="description"
						cols="30"
						rows="10"
						class="border p-2"
                        @input="description.errorMessage = ''"
                        v-model="description.value"
					></textarea>
                    <span
                        class="text-xs lg:text-sm text-red-500"
                        v-if="description.errorMessage"
                        >{{ description.errorMessage }}</span>
				</div>

				<div class="flex flex-col gap-1">
					<label for="demand" class="max-w-fit"
						>Yêu cầu ứng viên</label
					>
					<textarea
						name=""
						id="demand"
						cols="30"
						rows="10"
						class="border p-2"
                        @input="demand.errorMessage = ''"
                        v-model="demand.value"
					></textarea>
                    <span
                        class="text-xs lg:text-sm text-red-500"
                        v-if="demand.errorMessage"
                        >{{ demand.errorMessage }}</span>
				</div>

				<div class="flex flex-col gap-1">
					<label for="benefit" class="max-w-fit"
						>Quyền lợi ứng viên</label
					>
					<textarea
						name=""
						id="benefit"
						cols="30"
						rows="10"
						class="border p-2"
                        @input="benefit.errorMessage = ''"
                        v-model="benefit.value"
					></textarea>
                    <span
                        class="text-xs lg:text-sm text-red-500"
                        v-if="benefit.errorMessage"
                        >{{ benefit.errorMessage }}</span>
				</div>

				<button
					class="self-end place-self-end bg-green-400 px-4 py-2 rounded-xl text-sky-950 font-semibold hover:cursor-pointer hover:bg-green-500 hover:text-sky-900"
					@click="handleSubmit"
				>
					Xác nhận
				</button>
			</form>
		</section>
	</main>
</template>

<script lang="ts">
export default {
	data() {
		return {
			newSkill: "",
			skills: { value: [] as string[], isValid: true, errorMessage: "" },
			role: { value: "", isValid: true, errorMessage: "" },
			level: { value: "", isValid: true, errorMessage: "" },
			quantity: { value: "", isValid: true, errorMessage: "" },
			address: { value: "", isValid: true, errorMessage: "" },
			salary: { value: "", isValid: true, errorMessage: "" },
			description: { value: "", isValid: true, errorMessage: "" },
			demand: { value: "", isValid: true, errorMessage: "" },
			benefit: { value: "", isValid: true, errorMessage: "" },
		};
	},
	methods: {
		addSkill() {
			if (this.newSkill == "") return;

			this.skills.value.push(this.newSkill);
			this.newSkill = "";
		},
		deleteSkill(index: number) {
			this.skills.value.splice(index, 1);
		},
		validate() {
			this.skills.isValid = this.skills.value.length > 0;
			this.skills.errorMessage = this.skills.isValid
				? ""
				: "Vui lòng nhập ít nhất 1 kỹ năng yêu cầu";

			this.role.isValid = this.role.value.length > 0;
			this.role.errorMessage = this.role.isValid
				? ""
				: "Vui lòng nhập vị trí tuyển dụng";

			this.level.isValid = this.level.value.length > 0;
			this.level.errorMessage = this.level.isValid
				? ""
				: "Vui lòng nhập trình độ tuyển dụng";

			this.quantity.isValid = this.quantity.value.length > 0;
			this.quantity.errorMessage = this.quantity.isValid
				? ""
				: "Vui lòng nhập số lượng tuyển dụng";

			this.address.isValid = this.address.value.length > 0;
			this.address.errorMessage = this.address.isValid
				? ""
				: "Vui lòng nhập địa chỉ làm việc";

			this.salary.isValid = this.salary.value.length > 0;
			this.salary.errorMessage = this.salary.isValid
				? ""
				: "Vui lòng nhập mức lương";

			this.description.isValid = this.description.value.length > 0;
			this.description.errorMessage = this.description.isValid
				? ""
				: "Vui lòng nhập mô tả công việc";

			this.demand.isValid = this.demand.value.length > 0;
			this.demand.errorMessage = this.demand.isValid
				? ""
				: "Vui lòng nhập yêu cầu ứng viên";

			this.benefit.isValid = this.benefit.value.length > 0;
			this.benefit.errorMessage = this.benefit.isValid
				? ""
				: "Vui lòng nhập quyền lợi ứng viên";

			return (
				this.skills.isValid &&
				this.role.isValid &&
				this.level.isValid &&
				this.quantity.isValid &&
				this.address.isValid &&
				this.salary.isValid &&
				this.description.isValid &&
				this.demand.isValid &&
				this.benefit.isValid
			);
		},
		handleSubmit() {
			if (!this.validate()) return;

			// logic here
            console.log(this.role.value);
            
		},
	},
};
</script>
