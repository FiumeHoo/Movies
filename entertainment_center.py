import fresh_tomatoes
import media

thor = media.Movie('Thor: Ragnarok Teaser',
          'Thor battles Hulk.',
          'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1492753237992&di=b700d006f690e84ad785b77a15049b2c&imgtype=0&src=http%3A%2F%2Fwww.dzyule.com%2Fuploadfile%2F2015%2F1016%2F20151016092546775.jpg',
          '/watch?v=v7MGUNV8MxU&index=1&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi')

transformers = media.Movie('Transformers 5',
                'Humans and Transformers are at war, Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth.',
                'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1492753835727&di=f4d10e890736cfc10a17f176edcaba9f&imgtype=0&src=http%3A%2F%2Fpic.77ds.net%3A878%2Fpic%2Fcai%2F201609%2Ftv%2F2015-10%2F60608.jpg',
                '/watch?v=OnvPhdmp6BE&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi&index=19')

smurfs = media.Movie('Smurfs: The Lost Village',
                'In this fully animated, all-new take on the Smurfs, a mysterious map sets Smurfette and her friends Brainy, Clumsy and Hefty on an exciting race through the Forbidden Forest leading to the discovery of the biggest secret in Smurf history.',
                'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1492754534153&di=4aecfbeacb10b3e70a55ec5665fd24d9&imgtype=0&src=http%3A%2F%2Fi-4.yxdown.com%2F2016%2F9%2F21%2Fc5dbb49b-0f85-4813-8617-ec000e925422.jpg',
                '/watch?v=pknz-qempok&index=29&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi')

moana = media.Movie('Moana',
                "In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches an impetuous Chieftain's daughter's island, she answers the Ocean's call to seek out the Demigod to set things right.",
                'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1492754796698&di=e51583077a391ff8ea194f207e8b7706&imgtype=0&src=http%3A%2F%2Fv3img.osscdn.ifensi.com%2Fxw_imgs%2F2016%2F10%2F24%2F23eb8f10ab3c5.jpg',
                '/watch?v=lAkw1M2G5y8&index=32&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi')

zootopia = media.Movie('Zootopia',
                'In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.',
                'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1492754969816&di=6133cfe47ffde08b9568543b571e3164&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201603%2F31%2F20160331160753_K3WwA.thumb.700_0.jpeg',
                '/watch?v=J0hx9HmoXu4&index=34&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi')

despicable_me = media.Movie('Despicable Me 3',
                "Balthazar Bratt, a child star from the 1980's, hatches a scheme for world domination.",
                'http://www.hachettebookgroup.com/_b2c/media/cache/55/db/55db8e0cbb591cb109b2512a1bcc0c65.jpg',
                '/watch?v=6DBi41reeF0&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi&index=90')

movies = [thor, transformers, smurfs, moana, zootopia, despicable_me]
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)