<template>
	<section
		class="fixed top-0 left-0 right-0 h-full z-50 bg-white flex items-center justify-center"
	>
		<div
			class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 max-h-screen"
		>
			<div
				@submit.prevent="submitForm"
				class="w-full bg-gray- rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 bg-sky-200 dark:border-gray-700 max-h-screen"
			>
				<div class="p-6 space-y-4 md:space-y-6 sm:p-8">
					<h1
						class="text-xl font-bold leading-tight tracking-tight md:text-2xl text-cyan-900"
					>
						Tạo tài khoản và đăng nhập Head Hunter luôn nào !
					</h1>
					<form
						class="grid grid-cols-2 items-center gap-4"
						action="#"
					>
						<div>
							<label
								for="email"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Email:
							</label>
							<input
								type="email"
								name="email"
								id="email"
								class="bg-cyan-600 border border-gray-300 text-gray-300 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								placeholder="company-name@email.com"
								required="true"
								v-model="email.value"
								@input="email.error = ''"
							/>
							<span
								class="text-xs lg:text-sm text-red-500"
								v-if="email.error"
								>{{ email.error }}</span
							>
						</div>
						<div>
							<label
								for="password"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Mật khẩu</label
							>
							<input
								type="password"
								name="password"
								id="password"
								placeholder="••••••••"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="password.value"
								@input="password.error = ''"
							/>
							<span
								class="text-xs lg:text-sm text-red-500"
								v-if="password.error"
								>{{ password.error }}</span
							>
						</div>
						<div>
							<label
								for="repassword"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Xác nhận mật khẩu</label
							>
							<input
								type="password"
								name="repassword"
								id="repassword"
								placeholder="••••••••"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="repassword.value"
								@input="repassword.error = ''"
							/>
							<span
								class="text-xs lg:text-sm text-red-500"
								v-if="repassword.error"
								>{{ repassword.error }}</span
							>
						</div>

						<div>
							<label
								for="company_name"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Tên công ty</label
							>
							<input
								type="text"
								name="company_name"
								id="company_name"
								placeholder="Công ty ABC"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="company_name.value"
								@input="company_name.error = ''"
							/>
							<span
								class="text-xs lg:text-sm text-red-500"
								v-if="company_name.error"
								>{{ company_name.error }}</span
							>
						</div>

						<div>
							<label
								for="address"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Địa chỉ:
							</label>
							<input
								type="text"
								name="address"
								id="address"
								placeholder="Cau Giay, Ha Noi"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="address"
							/>
						</div>

						<div>
							<label
								for="founded_year"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Năm thành lập:
							</label>
							<input
								type="number"
								name="founded_year"
								id="founded_year"
								placeholder="1880"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="founded_year"
							/>
						</div>

						<div>
							<label
								for="employee_quantity"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Số lượng nhân viên:
							</label>
							<input
								type="number"
								name="employee_quantity"
								id="employee_quantity"
								placeholder="1000+"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="employee_quantity"
							/>
						</div>

						<div>
							<label
								for="contact"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Liên hệ:
							</label>
							<input
								type="text"
								name="contact"
								id="contact"
								placeholder="company@gmail.com"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
								v-model="contact"
							/>
						</div>

						<button
							type="submit"
							class="w-full text-white bg-cyan-800 hover:bg-cyan-900 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 col-span-2"
						>
							Đăng ký
						</button>

						<p class="text-sm font-light text-cyan-800 col-span-2">
							Bạn đã có tài khoản ?
							<a
								href="#"
								class="font-bold text-primary-600 hover:underline dark:text-primary-500"
							>
								<router-link to="/login/employee">
									Đăng nhập ngay !
								</router-link>
							</a>
						</p>
					</form>
				</div>
			</div>
		</div>
		<base-spinner v-if="isLoading"></base-spinner>
	</section>
</template>

<script lang="ts">
export default {
	data() {
		return {
			email: {
				value: "",
				error: "",
			},
			password: {
				value: "",
				error: "",
			},
			repassword: {
				value: "",
				error: "",
			},
			company_name: {
				value: "",
				error: "",
			},
			address: "",
			founded_year: 0,
			employee_quantity: 0,
			contact: "",
			isLoading: false,
		};
	},
	methods: {
		async submitForm() {
			if (this.isFormValid) {
				const formRegister = {
					fullname: "string",
					image_path: "string",
					email: this.email.value,
					password: this.password.value,
					date_of_birth: "2023-12-07T02:50:26.348Z",
					gender: "male",
					role: "hr",
					phone: "string",
				};
				const formCreateCompany = {
					job_quantity: 0,
					name: this.company_name.value,
					address: this.address,
					founded_year: this.founded_year,
					employee_quantity: this.employee_quantity,
					description: "abc",
					contact: this.contact,
				};

				let user_id = "";

				this.isLoading = true;
				try {
					const res = await this.$store.dispatch("registerCompany", {
						formRegister,
					});
					user_id = res.user_id;
					console.log("register success");
				} catch (err) {
					console.log(err);
				}

				try {
					await this.$store.dispatch("companies/createCompany", {
						...formCreateCompany,
						user_id,
					});

					console.log("create company success");
					this.resetForm();
				} catch (err) {
					console.log(err);
				}

				this.isLoading = false;
			}
		},
		resetForm() {
			this.email.value = "";
			this.password.value = "";
			this.repassword.value = "";
			this.company_name.value = "";
			this.address = "";
			this.founded_year = 0;
			this.employee_quantity = 0;
			this.contact = "";
		},
	},
	computed: {
		isFormValid() {
			if (this.email.value === "") {
				this.email.error = "Email không được để trống";
			} else {
				this.email.error = "";
			}

			if (this.password.value === "") {
				this.password.error = "Mật khẩu không được để trống";
			} else if (this.password.value.length < 6) {
				this.password.error = "Mật khẩu phải có ít nhất 6 ký tự";
			} else {
				this.password.error = "";
			}

			if (this.repassword.value === "") {
				this.repassword.error = "Xác nhận mật khẩu không được để trống";
			} else if (this.repassword.value !== this.password.value) {
				this.repassword.error = "Xác nhận mật khẩu không khớp";
			} else {
				this.repassword.error = "";
			}

			if (this.company_name.value === "") {
				this.company_name.error = "Tên công ty không được để trống";
			} else {
				this.company_name.error = "";
			}

			if (
				this.email.error === "" &&
				this.password.error === "" &&
				this.repassword.error === "" &&
				this.company_name.error === ""
			) {
				return true;
			} else {
				return false;
			}
		},
	},
};
</script>

<style scoped>
.form-register {
	min-width: 1000px;
}
</style>
