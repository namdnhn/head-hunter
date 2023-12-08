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
					<span class="flex items-center gap-2">
						<label for="role" class="max-w-fit"
							>Vị trí tuyển dụng</label
						>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="role.errorMessage"
							>{{ role.errorMessage }}</span
						>
					</span>
					<input
						type="text"
						id="role"
						class="border border-gray-300 p-2 rounded-md w-full"
						placeholder="VD: Backend Developer"
						@input="role.errorMessage = ''"
						v-model="role.value"
					/>
				</div>

				<div class="flex flex-col gap-1">
					<span class="flex items-center gap-2">
						<label for="level" class="max-w-fit">Trình độ</label>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="level.errorMessage"
							>{{ level.errorMessage }}</span
						>
					</span>
					<!-- <input
						type="text"
						id="level"
						placeholder="VD: Senior"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="level.errorMessage = ''"
						v-model="level.value"
					/> -->
					<select
						name=""
						id="level"
						class="border border-gray-300 p-2 rounded-md w-full"
						v-model="level.value"
					>
						<option value="intern">Intern</option>
						<option value="junior">Junior</option>
						<option value="middle">Middle</option>
						<option value="senior">Senior</option>
						<option value="lead">Lead</option>
						<option value="manager">Manager</option>
					</select>
				</div>

				<div class="flex flex-col gap-1">
					<span class="flex items-center gap-2">
						<label for="quantity" class="max-w-fit"
							>Số lượng tuyển dụng</label
						>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="quantity.errorMessage"
							>{{ quantity.errorMessage }}</span
						>
					</span>
					<input
						type="text"
						id="quantity"
						placeholder="VD: 4"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="quantity.errorMessage = ''"
						v-model="quantity.value"
					/>
				</div>

				<div class="flex flex-col gap-1">
					<span class="flex items-center gap-2">
						<label for="address" class="max-w-fit"
							>Địa chỉ làm việc</label
						>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="address.errorMessage"
							>{{ address.errorMessage }}</span
						>
					</span>
					<input
						type="text"
						id="address"
						placeholder="VD: Tầng 19, Leadvisors Tower, 643 Phạm Văn Đồng, Bắc Từ Liêm"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="address.errorMessage = ''"
						v-model="address.value"
					/>
				</div>

				<div class="flex flex-col gap-1">
					<span class="flex items-center gap-2">
						<label for="salary" class="max-w-fit">Mức lương</label>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="salary.errorMessage"
							>{{ salary.errorMessage }}</span
						>
					</span>
					<input
						type="text"
						id="salary"
						placeholder="VD: 1k$ - 2k$"
						class="border border-gray-300 p-2 rounded-md w-full"
						@input="salary.errorMessage = ''"
						v-model="salary.value"
					/>
				</div>

				<div class="flex flex-col gap-1">
					<span class="flex items-center gap-2">
						<label class="max-w-fit">Trạng thái công việc</label>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="deadline.errorMessage"
							>{{ deadline.errorMessage }}</span
						>
					</span>
					<div
						class="border border-gray-300 p-2 rounded-md w-full grid grid-cols-2"
					>
						<span class="flex gap-2 items-center">
							<label for="urgent">Tuyển gấp</label>
							<input
								type="checkbox"
								id="urgent"
								v-model="urgent"
							/>
						</span>
						<span class="flex gap-2 items-center">
							<label for="">Ngày hết hạn</label>
							<input
								type="date"
								class="px-2 border"
								v-model="deadline.value"
								@input="deadline.errorMessage = ''"
							/>
						</span>
					</div>
				</div>

				<div class="flex flex-col gap-1 border p-2 rounded-md">
					<span class="flex items-center gap-2">
						<label class="max-w-fit">Mô tả công việc</label>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="description.errorMessage"
							>{{ description.errorMessage }}</span
						>
					</span>
					<div v-for="(_, index) in description.value" :key="index">
						<span class="flex items-center gap-2">
							<input
								type="text"
								v-model="description.value[index]"
								class="border border-gray-300 p-2 rounded-md w-full"
								placeholder="Nhập mô tả công việc..."
								@input="description.errorMessage = ''"
							/>
							<font-awesome-icon
								icon="fa-solid fa-xmark"
								class="hover:cursor-pointer"
								@click="removeDescription(index)"
							/>
						</span>
					</div>
					<span
						@click="addDescription"
						class="bg-sky-300 max-w-fit px-2 rounded text-sky-900 hover:cursor-pointer"
						>Thêm đoạn văn</span
					>
				</div>

				<div class="flex flex-col gap-1 border p-2 rounded-md">
					<span class="flex items-center gap-2">
						<label class="max-w-fit">Yêu cầu ứng viên</label>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="demand.require.errorMessage"
							>{{ demand.require.errorMessage }}</span
						>
					</span>
					<div
						v-for="(_, index) in demand.require.value"
						:key="index"
					>
						<span class="flex items-center gap-2">
							<input
								type="text"
								v-model="demand.require.value[index]"
								class="border border-gray-300 p-2 rounded-md w-full"
								placeholder="Nhập yêu cầu ứng viên..."
								@input="demand.require.errorMessage = ''"
							/>
							<font-awesome-icon
								icon="fa-solid fa-xmark"
								class="hover:cursor-pointer"
								@click="removeRequire(index)"
							/>
						</span>
					</div>
					<span
						@click="addRequire"
						class="bg-sky-300 max-w-fit px-2 rounded text-sky-900 hover:cursor-pointer"
						>Thêm yêu cầu</span
					>
				</div>

				<div class="flex flex-col gap-1 border p-2 rounded-md">
					<span class="flex items-center gap-2">
						<label class="max-w-fit"
							>Yêu cầu chi tiết công việc</label
						>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="demand.job.errorMessage"
							>{{ demand.job.errorMessage }}</span
						>
					</span>
					<div v-for="(_, index) in demand.job.value" :key="index">
						<span class="flex items-center gap-2">
							<input
								type="text"
								v-model="demand.job.value[index]"
								class="border border-gray-300 p-2 rounded-md w-full"
								placeholder="Nhập yêu cầu chi tiết cầu công việc..."
								@input="demand.job.errorMessage = ''"
							/>
							<font-awesome-icon
								icon="fa-solid fa-xmark"
								class="hover:cursor-pointer"
								@click="removeJob(index)"
							/>
						</span>
					</div>
					<span
						@click="addJob"
						class="bg-sky-300 max-w-fit px-2 rounded text-sky-900 hover:cursor-pointer"
						>Thêm yêu cầu</span
					>
				</div>

				<div class="flex flex-col gap-1 border p-2 rounded-md">
					<span class="flex items-center gap-2">
						<label class="max-w-fit"
							>Yêu cầu bằng cấp/kỹ năng</label
						>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="demand.degree_skills.errorMessage"
							>{{ demand.degree_skills.errorMessage }}</span
						>
					</span>
					<div
						v-for="(_, index) in demand.degree_skills.value"
						:key="index"
					>
						<span class="flex items-center gap-2">
							<input
								type="text"
								v-model="demand.degree_skills.value[index]"
								class="border border-gray-300 p-2 rounded-md w-full"
								placeholder="Nhập yêu cầu bằng cấp/kỹ năng..."
								@input="demand.degree_skills.errorMessage = ''"
							/>
							<font-awesome-icon
								icon="fa-solid fa-xmark"
								class="hover:cursor-pointer"
								@click="removeDegreeSkills(index)"
							/>
						</span>
					</div>
					<span
						@click="addDegreeSkill"
						class="bg-sky-300 max-w-fit px-2 rounded text-sky-900 hover:cursor-pointer"
						>Thêm yêu cầu</span
					>
				</div>

				<div class="flex flex-col gap-1 border p-2 rounded-md">
					<span class="flex items-center gap-2">
						<label class="max-w-fit">Quyền lợi của ứng viên</label>
						<span
							class="text-xs lg:text-sm text-red-500"
							v-if="benefit.errorMessage"
							>{{ benefit.errorMessage }}</span
						>
					</span>
					<div v-for="(_, index) in benefit.value" :key="index">
						<span class="flex items-center gap-2">
							<input
								type="text"
								v-model="benefit.value[index]"
								class="border border-gray-300 p-2 rounded-md w-full"
								placeholder="Nhập quyền lợi ứng viên..."
								@input="benefit.errorMessage = ''"
							/>
							<font-awesome-icon
								icon="fa-solid fa-xmark"
								class="hover:cursor-pointer"
								@click="removeBenefit(index)"
							/>
						</span>
					</div>
					<span
						@click="addBenefit"
						class="bg-sky-300 max-w-fit px-2 rounded text-sky-900 hover:cursor-pointer"
						>Thêm yêu cầu</span
					>
				</div>

				<button
					class="self-end place-self-end bg-green-400 px-4 py-2 rounded-xl text-sky-950 font-semibold hover:cursor-pointer hover:bg-green-500 hover:text-sky-900"
				>
					Xác nhận
				</button>
			</form>
		</section>
		<base-dialog
			:show="createSuccess"
			title="Tạo tin tuyển dụng thành công!"
			@close="confirm"
		>
			<p>Tin tuyển dụng của bạn đã được đăng.</p>
		</base-dialog>
        <base-dialog :show="!!createError" title="Tạo tin tuyển dụng thất bại!" @close="confirmError">
            <p>{{ createError }}</p>
        </base-dialog>
	</main>
</template>

<script lang="ts">
export default {
	props: ["id"],
	data() {
		return {
			newSkill: "",
			skills: { value: [] as string[], isValid: true, errorMessage: "" },
			role: { value: "", isValid: true, errorMessage: "" },
			level: { value: "intern", isValid: true, errorMessage: "" },
			quantity: { value: "", isValid: true, errorMessage: "" },
			address: { value: "", isValid: true, errorMessage: "" },
			salary: { value: "", isValid: true, errorMessage: "" },
			description: { value: [""], isValid: true, errorMessage: "" },
			demand: {
				require: {
					value: [""],
					isValid: true,
					errorMessage: "",
				},
				job: {
					value: [""],
					isValid: true,
					errorMessage: "",
				},
				degree_skills: {
					value: [""],
					isValid: true,
					errorMessage: "",
				},
			},
			benefit: { value: [""], isValid: true, errorMessage: "" },
			deadline: { value: "", isValid: true, errorMessage: "" },
			urgent: false,
			companyInfo: {
				company_name: "",
				company_logo: "",
				company_id: "",
			},
			isLoading: false,
			createSuccess: false,
            createError: null
		};
	},
	methods: {
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

			this.description.isValid =
				this.description.value.length > 0 &&
				this.description.value[0].length > 0;
			this.description.errorMessage = this.description.isValid
				? ""
				: "Vui lòng nhập mô tả công việc";

			this.demand.require.isValid =
				this.demand.require.value.length > 0 &&
				this.demand.require.value[0].length > 0;
			this.demand.require.errorMessage = this.demand.require.isValid
				? ""
				: "Vui lòng nhập yêu cầu ứng viên";

			this.demand.job.isValid =
				this.demand.job.value.length > 0 &&
				this.demand.job.value[0].length > 0;
			this.demand.job.errorMessage = this.demand.job.isValid
				? ""
				: "Vui lòng nhập yêu cầu chi tiết công việc";

			this.demand.degree_skills.isValid =
				this.demand.degree_skills.value.length > 0 &&
				this.demand.degree_skills.value[0].length > 0;
			this.demand.degree_skills.errorMessage = this.demand.degree_skills
				.isValid
				? ""
				: "Vui lòng nhập yêu cầu bằng cấp/kỹ năng";

			this.benefit.isValid =
				this.benefit.value.length > 0 &&
				this.benefit.value[0].length > 0;
			this.benefit.errorMessage = this.benefit.isValid
				? ""
				: "Vui lòng nhập quyền lợi ứng viên";

			this.deadline.isValid = this.deadline.value.length > 0;
			this.deadline.errorMessage = this.deadline.isValid
				? ""
				: "Vui lòng nhập ngày hết hạn";

			return (
				this.role.isValid &&
				this.level.isValid &&
				this.quantity.isValid &&
				this.address.isValid &&
				this.salary.isValid &&
				this.description.isValid &&
				this.demand.require.isValid &&
				this.demand.job.isValid &&
				this.demand.degree_skills.isValid &&
				this.benefit.isValid &&
				this.deadline.isValid
			);
		},
		async handleSubmit() {
			if (!this.validate()) {
				console.log("form invalid");

				return;
			}
			this.isLoading = true;
			// logic here
			try {
				let require = "";

				for (let i = 0; i < this.demand.require.value.length; i++) {
					require += `
                                    
                                    <li
										class="flex items-center gap-2"
									>
										<font-awesome-icon
											icon="fa-regular fa-circle-dot"
										/>
                                        
										<p>${this.demand.require.value[i]}</p>
                                        
									</li>
                                    
                                    `;
				}

				let job_detail = "";
				for (let i = 0; i < this.demand.job.value.length; i++) {
					job_detail += `
                                    
                                    <li
										class="flex items-center gap-2"
									>

										<font-awesome-icon
											icon="fa-regular fa-circle-dot"
										/>

										<p>
											${this.demand.job.value[i]}
										</p>

									</li>
                                    
                                    `;
				}

				let degree_skill = "";
				for (
					let i = 0;
					i < this.demand.degree_skills.value.length;
					i++
				) {
					degree_skill += `

                                    <li
										class="flex items-center gap-2"
									>
										<font-awesome-icon
											icon="fa-regular fa-circle-dot"
										/>
										<p>
											${this.demand.degree_skills.value[i]}
										</p>

									</li>
                                    
                                    `;
				}

				let description = "";
				for (let i = 0; i < this.description.value.length; i++) {
					description += ` 
                            <p class="leading-7">
                                ${this.description.value[i]}
                            </p>
                            `;
				}

				let benefit = "";
				for (let i = 0; i < this.benefit.value.length; i++) {
					benefit += ` 
                                <li
									class="flex items-center gap-2"
								>

									<font-awesome-icon
										icon="fa-regular fa-circle-dot"
									/>

									<p>
										${this.benefit.value[i]}
									</p>

								</li> 
                                
                                `;
				}

				const formData = {
					company_id: Number(this.$store.getters.companyId),
					level: this.level.value.toLowerCase(),
					role: this.role.value,
					require: require,
					job_detail: job_detail,
					degree_skill: degree_skill,
					salary: this.salary.value,
					benefit: benefit,
					urgent: this.urgent,
					featured: false,
					company_name: this.companyInfo.company_name || "default",
					company_logo: this.companyInfo.company_logo || "default",
					quantity: Number(this.quantity.value),
					address: this.address.value,
					description: description,
					posting_date: new Date().toISOString(),
					deadline: new Date(this.deadline.value).toISOString(),
				};

				await this.$store.dispatch("jobs/createJob", formData);

				console.log("create job success");
				this.createSuccess = true;
				this.resetForm();
			} catch (err: any) {
				console.log(err);
                this.createError = err
			}

			this.isLoading = false;
		},
		addDescription() {
			this.description.value.push("");
		},
		addRequire() {
			this.demand.require.value.push("");
		},
		addJob() {
			this.demand.job.value.push("");
		},
		addDegreeSkill() {
			this.demand.degree_skills.value.push("");
		},
		addBenefit() {
			this.benefit.value.push("");
		},

		//remove
		removeBenefit(index: number) {
			this.benefit.value.splice(index, 1);
		},
		removeDegreeSkills(index: number) {
			this.demand.degree_skills.value.splice(index, 1);
		},
		removeJob(index: number) {
			this.demand.job.value.splice(index, 1);
		},
		removeRequire(index: number) {
			this.demand.require.value.splice(index, 1);
		},
		removeDescription(index: number) {
			this.description.value.splice(index, 1);
		},
		resetForm() {
			this.skills.value = [];
			this.role.value = "";
			this.level.value = "";
			this.quantity.value = "";
			this.address.value = "";
			this.salary.value = "";
			this.description.value = [""];
			this.demand.require.value = [""];
			this.demand.job.value = [""];
			this.demand.degree_skills.value = [""];
			this.benefit.value = [""];
			this.deadline.value = "";
			this.urgent = false;
		},
        confirmError() {
            this.createError = null
        },
		async getCompanyInfo() {
			try {
				const res = await this.$store.dispatch(
					"companies/getCompany",
					this.id
				);
				this.companyInfo = {
					company_name: res.name,
					company_logo: res.logo,
					company_id: this.id,
				};
				console.log(this.companyInfo);
			} catch (err) {
				console.log(err);
			}
		},

		confirm() {
			this.createSuccess = false;
		},
	},
	mounted() {
		this.getCompanyInfo();
	},
};
</script>
