class Comment_in_post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_in_post')
    text = models.TextField()
    status = models.CharField(max_length=20, default='active')


def get_comments(request, post_id):
    comments = Comments.objects.filter(post=post_id)
    data = [{'text': comment.text, 'status': comment.status} for comment in comments]
    return JsonResponse(data, safe=False)


 status = models.CharField(max_length=20, default='active')


def change_comment_status(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        new_status = request.POST.get('status')

        try:
            Comments.objects.filter(post=post_id).update(status=new_status)
            return JsonResponse({'success': True, 'message': 'Статус комментариев обновлен.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Метод не разрешен.'})
