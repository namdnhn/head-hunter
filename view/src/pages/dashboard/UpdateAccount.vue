<template>
	<form
		@submit.prevent="updateInfo"
		class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10"
	>
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Cập nhật thông tin tài khoản
		</h1>
		<div
			class="w-full p-10 bg-white rounded-xl flex flex-col gap-4 text-xs md:text-sm lg:text-base"
		>
			<div class="flex flex-col gap-1 w-full">
				<label for="fullname">Họ và tên:</label>
				<input
					type="text"
					id="fullname"
					class="py-2 px-4 border rounded-md"
					v-model="fullnameCandidate.value"
				/>
			</div>
			<div class="flex flex-col gap-1 w-full">
				<label for="email">Email:</label>
				<input
					type="email"
					id="email"
					class="py-2 px-4 border rounded-md"
					v-model="registerEmailCandicate.value"
				/>
			</div>
			<div class="flex flex-col gap-1 w-full">
				<label for="dob">Ngày sinh:</label>
				<input
					type="date"
					id="dob"
					class="py-2 px-4 border rounded-md"
					v-model="dobCandidate.value"
				/>
			</div>
			<div class="flex flex-col gap-1 w-full">
				<label for="phone">Số điện thoại:</label>
				<input
					type="text"
					id="phone"
					class="py-2 px-4 border rounded-md"
					v-model="phoneCandidate.value"
				/>
			</div>
			<div class="flex flex-col gap-1 w-full">
				<label for="oldpass">Mật khẩu hiện tại:</label>
				<input
					type="password"
					id="oldpass"
					class="py-2 px-4 border rounded-md"
					placeholder="******"
					v-model="currentPassword"
				/>
			</div>
			<div class="flex flex-col gap-1 w-full">
				<label for="newpass">Mật khẩu mới:</label>
				<input
					type="password"
					id="newpass"
					class="py-2 px-4 border rounded-md"
					v-model="registerPasswordCandicate.value"
					@input="registerPasswordCandicate.isValid = true"
				/>
				<span
					class="text-xs lg:text-sm text-red-500"
					v-if="!registerPasswordCandicate.isValid"
					>Mật khẩu quá ngắn, hãy nhập lại</span
				>

				<span></span>
			</div>
			<div class="flex flex-col gap-1 w-full">
				<label for="confirmpass">Nhập lại mật khẩu:</label>
				<input
					type="password"
					id="confirmpass"
					class="py-2 px-4 border rounded-md"
					v-model="registerPasswordCandicateConfirm.value"
					@input="registerPasswordCandicateConfirm.isValid = true"
				/>
				<span
					class="text-xs lg:text-sm text-red-500"
					v-if="!registerPasswordCandicateConfirm.isValid"
					>Mật khẩu không trùng khớp, vui lòng thử lại</span
				>
			</div>
			<button
				class="py-2 px-6 bg-green-500 max-w-max rounded-xl text-white hover:bg-green-600"
			>
				Xác nhận
			</button>
		</div>
	</form>
	<base-spinner v-if="isLoading"></base-spinner>
	<base-dialog
		:show="!!error"
		title="Cập nhật thông tin thất bại!"
		@close="confirmError"
		><p>
			{{ error }}<br />
			Vui lòng thử lại.
		</p></base-dialog
	>
</template>

<script lang="ts">
export default {
	data() {
		return {
			dob: new Date().toISOString().slice(0, 10),
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
			currentPassword: "",
		};
	},
	methods: {
		validate() {
			this.formIsValid = true;
			if (this.registerEmailCandicate.value === "") {
				this.registerEmailCandicate.isValid = false;
				this.formIsValid = false;
				console.log("email false");
			}
			if (
				this.registerPasswordCandicate.value === "" ||
				this.registerPasswordCandicate.value.length < 8
			) {
				this.registerPasswordCandicate.isValid = false;
				this.formIsValid = false;
				console.log("pass false");
			}
			if (
				this.registerPasswordCandicateConfirm.value === "" ||
				this.registerPasswordCandicateConfirm.value.length < 8 ||
				this.registerPasswordCandicateConfirm.value !==
					this.registerPasswordCandicate.value
			) {
				this.registerPasswordCandicateConfirm.isValid = false;
				this.formIsValid = false;
				console.log("confirm false");
			}
			if (this.fullnameCandidate.value === "") {
				this.fullnameCandidate.isValid = false;
				this.formIsValid = false;
				console.log("fullname false");
			}
			if (this.phoneCandidate.value === "") {
				this.phoneCandidate.isValid = false;
				this.formIsValid = false;
				console.log("phone false");
			}
			if (this.dobCandidate.value === "") {
				this.dobCandidate.isValid = false;
				this.formIsValid = false;
				console.log("dob false");
			}
		},
		async getUserInfo() {
			if (this.isLoggedIn) {
				const userId = this.$store.getters.userId;
				try {
					await this.$store.dispatch("fetchUserById", userId);
					const data = this.$store.getters.getUserInfo;
					data.date_of_birth = new Date(data.date_of_birth)
						.toISOString()
						.slice(0, 10);
					this.registerEmailCandicate.value = data.email;
					this.dobCandidate.value = data.date_of_birth;
					this.fullnameCandidate.value = data.fullname;
					this.phoneCandidate.value = data.phone;
				} catch (error: any) {
					console.log(error);
				}
			} else {
				return;
			}
		},
		async updateInfo() {
			this.validate();
			console.log("validate form update");

			if (!this.formIsValid) {
				return;
			}
			this.isLoading = true;
			const data = {
				fullname: this.fullnameCandidate.value,
				password: this.registerPasswordCandicate.value,
				phone: this.phoneCandidate.value,
				date_of_birth: new Date(this.dobCandidate.value).toISOString(),
				email: this.registerEmailCandicate.value,
			};

			try {
				await this.$store.dispatch("updateInfo", data);
				console.log("update info success");
			} catch (error: any) {
				console.log(error);
				this.error =
					error.message || "Có lỗi không xác định đã xảy ra!";
			}
			this.isLoading = false;
		},
		confirmError() {
			this.error = null;
		},
	},
	computed: {
		isLoggedIn() {
			return this.$store.getters.isAuthenticated;
		},
	},
	mounted() {
		this.getUserInfo();
	},
};
</script>
