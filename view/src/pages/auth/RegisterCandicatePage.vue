<template>
	<section class="pt-20 bg-lime-50">
		<div
			class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0"
		>
			<a
				href="#"
				class="flex items-center mb-6 text-2xl font-semibold text-cyan-900"
			>
				Trang đăng ký này dành riêng cho ứng viên
			</a>
			<div
				@submit.prevent="submitForm"
				class="w-full bg-gray- rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 bg-sky-200 dark:border-gray-700"
			>
				<div class="p-6 space-y-4 md:space-y-6 sm:p-8">
					<h1
						class="text-xl font-bold leading-tight tracking-tight md:text-2xl text-cyan-900"
					>
						Tạo tài khoản và đăng nhập Head Hunter luôn nào !
					</h1>
					<form class="space-y-4 md:space-y-6" action="#">
						<div>
							<label
								for="email"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Email của bạn</label
							>

							<input
								type="email"
								name="email"
								id="email"
								class="bg-cyan-600 border border-gray-300 text-gray-300 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
								placeholder="email@company.com"
								required="true"
								v-model="registerEmailCandicate.value"
							/>
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
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
								required="true"
								v-model="registerPasswordCandicate.value"
								@input="checkKeyDownPassword"
							/>
						</div>
						<div>
							<!-- <label v-if="checkKeyDown()"></label> -->
							<label
								class="block mb-2 text-sm font-medium text-red-500"
								v-if="!registerPasswordCandicate.isValid"
								>Mật khẩu của bạn quá ngắn, hãy nhập lại mật
								khẩu !</label
							>
						</div>
						<div>
							<label
								for="password"
								class="block mb-2 text-sm font-medium text-cyan-900"
								>Xác nhận mật khẩu</label
							>
							<input
								type="password"
								name="password"
								id="password"
								placeholder="••••••••"
								class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
								required="true"
								v-model="registerPasswordCandicateConfirm.value"
								@input="checkKeyDownPasswordConfirm"
							/>
						</div>
						<div>
							<!-- <label v-if="checkKeyDown()"></label> -->
							<label
								class="block mb-2 text-sm font-medium text-red-500"
								v-if="!registerPasswordCandicateConfirm.isValid"
								>Mật khẩu không khớp với mật khẩu đăng ký</label
							>
						</div>
						<div class="flex items-center justify-between">
							<div class="flex items-start">
								<div class="flex items-start">
									<div class="flex items-center h-5">
										<input
											id="terms"
											aria-describedby="terms"
											type="checkbox"
											class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
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
								<router-link to="./loginCandicatePage"
									>Đăng nhập ngay !</router-link
								>
							</a>
						</p>
					</form>
				</div>
			</div>
		</div>
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
			formIsValid: true,
            error: null,
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
				this.registerPasswordCandicateConfirm.value !=
					this.registerPasswordCandicate.value
			) {
				this.registerPasswordCandicateConfirm.isValid = false;
				this.formIsValid = false;
			}
		},
		async submitForm() {
			this.validateForm();
			if (!this.formIsValid) {
				return;
			}

			const formRegisterCandicate = {
				email: this.registerEmailCandicate.value,
				password: this.registerPasswordCandicate.value,
				fullname: "none",
				date_of_birth: "2023-10-18T18:53:43.235Z",
				role: "candidate",
				phone: "none"
			};

            console.log('form vuex');
            
			try {
                // handle register
                const payload = {
                    ...formRegisterCandicate,
                    mode: 'register'
                }
                await this.$store.dispatch("auth", payload);
                console.log('success vuex');
                
			} catch (error) {
				console.log(error);
			}
		},
		checkKeyDownPassword() {
			this.registerPasswordCandicate.isValid = true;
		},
		checkKeyDownPasswordConfirm() {
			this.registerPasswordCandicateConfirm.isValid = true;
		},
	},
};
</script>
