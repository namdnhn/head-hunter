<template>
	<main class="pt-16 lg:pt-20 w-full">
		<section class="py-10 w-full">
			<div class="container w-full">
				<div class="row">
					<div class="col-sm-12">
						<div class="col-sm-10 col-sm-offset-1 text-center">
							<div class="four_zero_four_bg">
								<h1
									class="text-center text-green-500 font-bold text-5xl"
								>
									404
								</h1>
							</div>

							<div
								class="flex flex-col justify-center items-center gap-4"
							>
								<h3
									class="text-xl md:text-2xl lg:text-2xl text-green-700"
								>
									Trang bạn tìm kiếm không tồn tại!
								</h3>

								<router-link
									to="/"
									class="bg-green-300 p-4 max-w-max rounded-lg text-sky-900 hover:cursor-pointer hover:bg-green-400 hover:text-sky-900"
									>Trở về trang chủ</router-link
								>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
	</main>
</template>

<style scoped>
.four_zero_four_bg {
	background-image: url(https://cdn.dribbble.com/users/285475/screenshots/2083086/dribbble_1.gif);
	height: 400px;
	background-position: center;
}
</style>
