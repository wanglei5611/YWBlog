from django.utils.safestring import mark_safe

class Page(object):
    def __init__(self, current_page, total, page_data_size=10, page_box_size=5):
        '''
            current_page	当前页码
            total 			数据总数
            per_page_size   每页显示多少条数据
            page_num		分页条长度
    	'''
        self.current_page = current_page
        self.total = total
        self.page_data_size = page_data_size
        self.page_box_size = page_box_size

    @property
    def start(self):
        return (self.current_page - 1) * self.page_data_size

    @property
    def end(self):
        return self.current_page * self.page_data_size

    def page_str(self, url):
        # 总页数
        total_page, y = divmod(self.total, self.page_data_size)

        if y:
            total_page += 1

        page_list = []

        # 总页数是否小于分页条长度
        if total_page < self.page_box_size:
            start_index = 1
            end_index = total_page + 1
        else:
            if self.current_page <= (self.page_box_size + 1) / 2:
                start_index = 1
                end_index = self.page_box_size + 1
            else:
                start_index = self.current_page - (self.page_box_size - 1) / 2
                end_index = self.current_page + (self.page_box_size - 1) / 2 + 1
                if self.current_page + (self.page_box_size - 1) / 2 > total_page:
                    start_index = total_page - (self.page_box_size - 1)
                    end_index = total_page + 1

        # 遍历组合页码条
        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = f'<a class="active" href="{url}?page={i}">{i}</a>'
            else:
                temp = f'<a href="{url}?page={i}">{i}</a>'
            page_list.append(temp)

        # 上一页,下一页
        if not self.current_page == 1:
            page_list.insert(0, f'<a href="{url}?page=%s">上一页</a>' % (self.current_page - 1))
        if not self.current_page == total_page:
            page_list.append(f'<a href="{url}?page=%s">下一页</a>' % (self.current_page + 1))

        page_list = ''.join(page_list)

        return mark_safe(page_list)
