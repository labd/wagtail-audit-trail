from django.utils.encoding import force_text

from wagtail.admin import compare


def page_revision_diff(revision_a, revision_b):
    comparison = [
        comp(revision_a, revision_b)
        for comp in revision_b.get_edit_handler().get_comparison()
    ]
    comparison = [comp for comp in comparison if comp.has_changed()]

    result = []
    for comp in comparison:
        item = {
            'label': force_text(comp.field_label()),
        }

        if isinstance(comp, compare.StreamFieldComparison):
            item['diff'] = comp.htmldiff()

        elif comp.is_field:
            item['diff'] = comp.htmldiff()
        elif comp.is_child_relation():
            item['children'] = []

            for child_comp in comp.get_child_comparisons():
                item_child = {
                    'move': child_comp.get_position_change(),
                    'operation': '',
                    'fields': []
                }

                if child_comp.is_addition:
                    item_child['operation'] = 'addition'
                if child_comp.is_deletion:
                    item_child['operation'] = 'deletion'

                for child_field_comp in child_comp.get_field_comparisons():
                    item_child['fields'].append({
                        'label': child_field_comp.field_label,
                        'htmldiff': child_field_comp.htmldiff
                    })
                item['children'].append(item_child)

        result.append(item)
    return result
