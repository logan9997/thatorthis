from django.shortcuts import redirect
from ..models import (
    Comment as CommentModel,
    CommentVote as CommentVoteModel
)
from ..forms import (
    Comment as CommentForm, 
    CommentVote as CommentVoteForm,
    DeleteComment
)
from ..utils import Vote, text_filter

def comment(request, post_id):

    user_id = request.session.get('user_id', -1)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            comment = text_filter(comment)

            new_comment = CommentModel(
                post_id=post_id,
                user_id=user_id,
                comment=comment
            )
            new_comment.save()

    return redirect('post', post_id)


def comment_vote(request, comment_id, post_id):

    user_id = request.session.get('user_id', -1)

    if request.method == 'POST':
        form = CommentVoteForm(request.POST)
        if form.is_valid():
           Vote.vote_handler(
               request, 
               form, 
               comment_id, 
               user_id, 
               CommentVoteModel
            )

    return redirect('post', post_id)


def delete_comment(request, comment_id, post_id):

    if request.method == 'POST':
        form = DeleteComment(request.POST)
        if form.is_valid():
            delete = form.cleaned_data.get('delete_comment')

            if delete:
                comment = CommentModel.objects.filter(comment_id=comment_id)
                comment.delete()
    return redirect('post', post_id)