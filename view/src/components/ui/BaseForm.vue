<template>
	<teleport to="body">
		<div
			v-if="show"
			@click="tryClose"
			class="fixed top-0 left-0 w-full h-screen z-50 backdrop"
		></div>
		<transition name="dialog">
			<div
				class="fixed top-0 left-0 w-full h-full flex items-center justify-center z-50"
				v-if="show"
			>
				<form
					@submit.prevent=""
					class="p-4 flex flex-col gap-4 rounded-lg bg-white"
				>
					<div class="flex justify-between items-center">
						<h1
							class="text-lg md:text-xl lg:text-2xl font-bold text-sky-900"
						>
							Ứng tuyển
						</h1>
						<font-awesome-icon
							icon="fa-solid fa-xmark"
							class="text-base md:text-lg lg:text-xl hover:cursor-pointer hover:text-green-500"
							@click="tryClose"
						/>
					</div>
					<h2 class="text-sm md:text-base lg:text-lg text-sky-800">
						Thông tin hồ sơ
					</h2>
					<div class="flex flex-col gap-1">
						<label for="fullname" class="text-xs lg:text-sm"
							>Họ và tên:</label
						>
						<input
							type="text"
							id="fullname"
							class="p-2 border border-black rounded-lg text-xs md:text-sm lg:text-base"
							v-model="userInfo.fullname"
						/>
					</div>
					<div class="flex flex-col gap-1">
						<label for="email" class="text-xs lg:text-sm"
							>Email:</label
						>
						<input
							type="email"
							id="email"
							class="p-2 border border-black rounded-lg text-xs md:text-sm lg:text-base"
							v-model="userInfo.email"
						/>
					</div>
					<div class="flex flex-col gap-1">
						<label
							for="resume"
							class="text-xs lg:text-sm inline-block max-w-max"
							>CV của bạn:</label
						>
						<input
							type="file"
							id="resume"
							class="text-xs lg:text-sm max-w-max"
							accept=".pdf"
						/>
					</div>
					<div class="flex flex-col gap-1">
						<label for="letter" class="text-xs lg:text-sm"
							>Giới thiệu bản thân:</label
						>
						<textarea
							name="letter"
							id="letter"
							cols="30"
							rows="5"
							class="p-2 border border-black rounded-md text-xs md:text-sm lg:text-base"
						></textarea>
					</div>
					<p class="text-xs lg:text-sm italic">
						Hồ sơ trên trang cá nhân của bạn sẽ được gửi kèm theo
						mẫu đơn này.
						<router-link to="/profile" class="text-red-600"
							>Kiểm tra lại</router-link
						>
					</p>
					<button
						class="bg-green-400 text-sky-900 font-bold p-2 rounded-lg hover:cursor-pointer hover:bg-green-500 hover:text-sky-950 text-xs md:text-sm lg:text-base"
						@click="tryClose"
					>
						Nộp đơn
					</button>
				</form>
			</div>
		</transition>
	</teleport>
</template>

<script lang="ts">
export default {
	props: {
		show: {
			type: Boolean,
			required: true,
		},
	},
	data() {
		return {
			userInfo: {
				fullname: "",
				email: "",
			},
		};
	},
	emits: ["close"],
	methods: {
		tryClose() {
			this.$emit("close");
		},
		async getUserInfo() {
			const data = this.$store.getters.getUserInfo;
			this.userInfo.fullname = data.fullname;
			this.userInfo.email = data.email;
		},
		validate() {
			if (!this.userInfo.fullname) {
				return false;
			}
			if (!this.userInfo.email) {
				return false;
			}
			return true;
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

<style scoped>
.backdrop {
	background-color: rgba(0, 0, 0, 0.75);
}

.dialog-enter-from,
.dialog-leave-to {
	opacity: 0;
	transform: scale(0.8);
}

.dialog-enter-to,
.dialog-leave-from {
	opacity: 1;
	transform: scale(1);
}

.dialog-enter-active {
	transition: all 0.3s ease-out;
}

.dialog-leave-active {
	transition: all 0.3s ease-in;
}
</style>
