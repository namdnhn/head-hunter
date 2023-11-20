<template>
	<form
		@submit.prevent=""
		class="p-8 md:basis-3/5 lg:basis-4/5 flex flex-col gap-10"
	>
		<h1 class="text-lg md:text-xl lg:text-2xl text-sky-900 font-bold">
			Xóa tài khoản
		</h1>
		<div
			class="w-full p-10 bg-white rounded-xl flex flex-col gap-4 text-xs md:text-sm lg:text-base"
		>
			<div class="flex gap-4 items-center w-80 md:w-96 justify-between">
				<label for="oldpass">Mật khẩu hiện tại:</label>
				<input type="password" class="py-2 px-4 border rounded-md" id="oldpass"/>
                
			</div>
			<button
				class="py-2 px-6 bg-red-600 max-w-max rounded-xl text-white hover:bg-green-600"
			>
				Xác nhận
			</button>
		</div>
	</form>
</template>
