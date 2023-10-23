<template>
	<section
		class="fixed top-0 left-0 right-0 h-full w-full z-40 bg-white flex items-center justify-center"
	>
		<div class="flex flex-col items-center justify-center mx-auto lg:py-0 w-full">
			<a
				href="#"
				class="flex items-center mb-6 text-base md:text-lg lg:text-xl font-semibold text-cyan-900"
			>
				Trang đăng ký này dành riêng cho ứng viên
			</a>
			<div
				@submit.prevent="submitForm"
				class="w-full bg-gray- rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 bg-sky-200 dark:border-gray-700"
			>
				<div class="p-6 space-y-4 md:space-y-6 sm:p-8">
					<h1
						class="font-bold leading-tight tracking-tight text-sm text-center md:text-base lg:text-lg text-cyan-900"
					>
						Tạo tài khoản và đăng nhập Head Hunter luôn nào!
					</h1>
					<form class="space-y-4 md:space-y-6 text-xs md:text-sm lg:text-base" action="#">
						<div class="flex gap-4">
							<span class="basis-1/2">
								<label
									for="email"
									class="block mb-2 font-medium text-cyan-900"
									>Email của bạn</label
								>

								<input
									type="email"
									name="email"
									id="email"
									class="bg-cyan-600 border border-gray-300 text-gray-300 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
									placeholder="email@company.com"
									required="true"
									v-model="registerEmailCandicate.value"
								/>
							</span>
							<span class="basis-1/2">
								<!-- fullname  -->
								<div>
									<label
										for="fullname"
										class="block mb-2  font-medium text-cyan-900"
										>Họ và tên</label
									>

									<input
										type="text"
										name="fullname"
										id="fullname"
										class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
										required="true"
										v-model="fullnameCandidate.value"
									/>
								</div>
							</span>
						</div>
						<div class="flex gap-4">
							<span class="basis-1/2">
								<label
									for="password"
									class="block mb-2  font-medium text-cyan-900"
									>Mật khẩu</label
								>
								<input
									type="password"
									name="password"
									id="password"
									placeholder="••••••••"
									class="bg-gray-50 border border-gray-300 text-gray-900  rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
									required="true"
									v-model="registerPasswordCandicate.value"
									@input="checkKeyDownPassword"
								/>
								<div>
									<!-- <label v-if="checkKeyDown()"></label> -->
									<label
										class="block mt-2 font-medium text-red-500"
										v-if="
											!registerPasswordCandicate.isValid
										"
										>Mật khẩu của bạn quá ngắn, hãy nhập lại
										mật khẩu !</label
									>
								</div>
							</span>
							<span class="basis-1/2">
								<label
									for="repassword"
									class="block mb-2  font-medium text-cyan-900"
									>Xác nhận mật khẩu</label
								>
								<input
									type="password"
									name="repassword"
									id="repassword"
									placeholder="••••••••"
									class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
									required="true"
									v-model="
										registerPasswordCandicateConfirm.value
									"
									@input="checkKeyDownPasswordConfirm"
								/>
								<div>
									<!-- <label v-if="checkKeyDown()"></label> -->
									<label
										class="block mt-2 font-medium text-red-500"
										v-if="
											!registerPasswordCandicateConfirm.isValid
										"
										>Mật khẩu không khớp với mật khẩu đăng
										ký</label
									>
								</div>
							</span>
						</div>

						<div class="flex gap-4">
							<!-- date of birth  -->
							<span class="basis-1/2">
								<label
									for="dob"
									class="block mb-2 font-medium text-cyan-900"
									>Ngày sinh</label
								>

								<input
									type="date"
									name="dob"
									id="dob"
									class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
									required="true"
									v-model="dobCandidate.value"
								/>
							</span>
							<!-- phone number  -->
							<span class="basis-1/2">
								<label
									for="phone"
									class="block mb-2 font-medium text-cyan-900"
									>Số điện thoại</label
								>

								<input
									type="text"
									name="phone"
									id="phone"
									class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"
									required="true"
									v-model="phoneCandidate.value"
								/>
							</span>
						</div>

						<div class="flex items-center justify-between">
							<div class="flex items-start">
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="terms"
											aria-describedby="terms"
											type="checkbox"
											class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800 "
											required="true"
										/>
									</div>
									<div class="ml-3 text-sm">
										<label
											for="terms"
											class="font-light text-cyan-900"
											>Tôi đồng ý với
											<a
												class="font-medium text-primary-600 hover:underline dark:text-primary-500"
												href="#"
												required="true"
												>Điều khoản và điều kiện của
												Head Hunter</a
											></label
										>
									</div>
								</div>
							</div>
						</div>

						<button
							type="submit"
							class="w-full text-white bg-cyan-800 hover:bg-cyan-900 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2"
						>
							Đăng ký
						</button>

						<p class="text-sm font-light text-cyan-800">
							Bạn đã có tài khoản ?
							<a
								href="#"
								class="font-bold text-primary-600 hover:underline dark:text-primary-500"
							>
								<router-link to="./loginCandidatePage"
									>Đăng nhập ngay !</router-link
								>
							</a>
						</p>
					</form>
				</div>
			</div>
		</div>
		<base-dialog
			:show="!!error"
			title="Đăng kí thất bại!"
			@close="handleError"
		>
			<p>
				{{ error }}<br />
				Vui lòng thử lại.
			</p>
		</base-dialog>
		<base-spinner v-if="isLoading"></base-spinner>
	</section>
</template>

<script lang="ts">
export default {
	data() {
		return {
			registerEmailCandicate: {
				value: "",
				isValid: true,
			},
			registerPasswordCandicate: {
				value: "",
				isValid: true,
				error: null,
			},
			registerPasswordCandicateConfirm: {
				value: "",
				isValid: true,
				error: null,
			},
			fullnameCandidate: {
				value: "",
				isValid: true,
				error: null,
			},
			phoneCandidate: {
				value: "",
				isValid: true,
				error: null,
			},
			dobCandidate: {
				value: "",
				isValid: true,
				error: null,
			},
			formIsValid: true,
			error: null,
			isLoading: false,
		};
	},
	methods: {
		validateForm() {
			this.formIsValid = true;
			if (this.registerEmailCandicate.value === "") {
				this.registerEmailCandicate.isValid = false;
				this.formIsValid = false;
			}
			if (
				this.registerPasswordCandicate.value === "" ||
				this.registerPasswordCandicate.value.length < 8
			) {
				this.registerPasswordCandicate.isValid = false;
				this.formIsValid = false;
			}
			if (
				this.registerPasswordCandicateConfirm.value === "" ||
				this.registerPasswordCandicateConfirm.value.length < 8 ||
				this.registerPasswordCandicateConfirm.value !==
					this.registerPasswordCandicate.value
			) {
				this.registerPasswordCandicateConfirm.isValid = false;
				this.formIsValid = false;
			}
			if (this.fullnameCandidate.value === "") {
				this.fullnameCandidate.isValid = false;
				this.formIsValid = false;
			}
			if (this.phoneCandidate.value === "") {
				this.phoneCandidate.isValid = false;
				this.formIsValid = false;
			}
			if (this.dobCandidate.value === "") {
				this.dobCandidate.isValid = false;
				this.formIsValid = false;
			}
		},
		async submitForm() {
			this.validateForm();
			if (!this.formIsValid) {
				return;
			}
			this.isLoading = true;

			const formRegisterCandicate = {
				email: this.registerEmailCandicate.value,
				password: this.registerPasswordCandicate.value,
				fullname: this.fullnameCandidate.value,
				date_of_birth: new Date(this.dobCandidate.value).toISOString(),
				phone: this.phoneCandidate.value,
			};

            console.log('form vuex');
            
			try {
				// handle register
				const payload = {
					...formRegisterCandicate,
					mode: "register",
				};
				await this.$store.dispatch("auth", payload);
				const redirectUrl =
					"/" + (this.$route.query.redirect || "homepage");
				this.$router.push(redirectUrl);
			} catch (error: any) {
				this.error = error.message || "Có lỗi không xác định đã xảy ra!";
			}

			this.isLoading = false;
		},
		checkKeyDownPassword() {
			this.registerPasswordCandicate.isValid = true;
		},
		checkKeyDownPasswordConfirm() {
			this.registerPasswordCandicateConfirm.isValid = true;
		},
		handleError() {
			this.error = null;
		},
	},
};
</script>
