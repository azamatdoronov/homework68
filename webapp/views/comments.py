from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from ..forms import CommentForm
from ..models import Article, Comment


class CreateCommentView(CreateView):
    form_class = CommentForm
    template_name = "comments/create.html"

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        user = self.request.user
        form.instance.article = article
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class UpdateComment(UserPassesTestMixin, UpdateView):
    form_class = CommentForm
    template_name = "comments/update.html"
    model = Comment

    def test_func(self):
        return self.get_object().author == self.request.user or \
               self.request.user.has_perm('webapp.change_comment')

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class DeleteComment(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class CreateLikeComment(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        comment = get_object_or_404(Comment, pk=pk)
        print(comment)
        user = self.request.user
        if comment.user.filter(id=user.pk):
            print(comment.user.filter(id=user.pk))
            comment.user.remove(user.pk)
        else:
            comment.user.add(user)
        likes = len(comment.user.all())
        param = {'likes': likes}
        return JsonResponse(param)
