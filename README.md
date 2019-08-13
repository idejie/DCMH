# DCMH
> Implement for Paper **CVPR 2017: [Deep Cross-Modal Hashing](https://arxiv.org/abs/1602.02255)**

### Dataset
- **MIRFLICKR-25K**: M. J. Huiskes, M. S. Lew (2008). [The MIR Flickr Retrieval Evaluation](The MIR Flickr Retrieval Evaluation). ACM International Conference on Multimedia Information Retrieval (MIR'08), Vancouver, Canada ([bib](https://lms.comp.nus.edu.sg/research/large-files/nuswide-civr2009.pdf))
- **IAPRTC12**: [The IAPR Benchmark: A New Evaluation Resource for Visual Information Systems](http://thomas.deselaers.de/publications/papers/grubinger_lrec06.pdf), Grubinger, Michael, Clough Paul D., Müller Henning, and Deselaers Thomas , International Conference on Language Resources and Evaluation, 24/05/2006, Genoa, Italy, (2006)
- **NUS-WIDE**: Tat-Seng Chua, Jinhui Tang, Richang Hong, Haojie Li, Zhiping Luo, and Yan-Tao Zheng. "NUS-WIDE: A Real-World Web Image Database from National University of Singapore", ACM International Conference on Image and Video Retrieval. Greece. Jul. 8-10, 2009. [*[pdf](https://lms.comp.nus.edu.sg/research/large-files/nuswide-civr2009.pdf)*] [[Bibitex entry](https://lms.comp.nus.edu.sg/research/large-files/nuswide-civr2009.pdf)]

*you can download above from [google drive](https://drive.google.com/open?id=1j0OJyuqwA1mySI4tQO9CvK0CL4qIYw-8)*
### Requirements
- Python 3.x or Anancoda 3.x

included in `requirements.txt` and `conda_env.yml`, you install them by:
```bash
$ pip install -r requirments.txt
# or
$ conda create -f environment.yml 
```


### Usage
```bash
$ python  main.py  train   --config  config/train.conf # for train
$ python  main.py  test  --config  config/test.conf # for test
```
### Configuration
- to add

### TO-DO

- [x] configuration

- [ ] data process

- [ ] base module

- [ ] text module/image module

- [ ] metrics

- [ ] other baseline models


### Thanks to

- [jiangqy/DCMH-CVPR2017](https://github.com/jiangqy/DCMH-CVPR2017):source code for paper "Deep Cross-Modal Hashing"
- [WendellGul/DCMH](https://github.com/WendellGul/DCMH):PyTorch implementation for paper "Deep Cross-Modal Hashing"
### Licences
 - to add