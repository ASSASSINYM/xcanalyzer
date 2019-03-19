from unittest import TestCase

from ..models import XcTarget, XcProject

from .fixtures import XcModelsFixture


class XcProjectTests(TestCase):

    fixture = XcModelsFixture()

    # __init__

    def test_instantiate_xc_project(self):
        xc_project = XcProject(name="MyXcProject", targets=set())

        self.assertTrue(xc_project)
        self.assertEqual(xc_project.name, "MyXcProject")

    def test_instantiate_xc_project__with_targets__has_targets(self):
        target = self.fixture.any_target()
        targets = set([target])
        
        xc_project = XcProject(name="MyXcProject", targets=targets)

        self.assertEqual(xc_project.targets, targets)

    # targets_of_type

    def test_targets_of_type__returns_filtered_target_by_type(self):
        target_1 = self.fixture.any_target(target_type=XcTarget.Type.UI_TEST)
        target_2 = self.fixture.any_target(target_type=XcTarget.Type.TEST)
        target_3 = self.fixture.any_target(target_type=XcTarget.Type.APPLICATION)
        targets = set([target_1, target_2, target_3])
        xc_project = XcProject(name="MyXcProject", targets=targets)

        targets = xc_project.targets_of_type(XcTarget.Type.UI_TEST)

        self.assertEqual(targets, [target_1])
    
    # target_with_name

    def test_target_with_name__returns_none__when_no_matching_target_name(self):
        target_1 = self.fixture.any_target(name='MyTarget1')
        xc_project = XcProject(name="MyXcProject", targets=set([target_1]))

        target_2 = xc_project.target_with_name('MyTarget2')

        self.assertIsNone(target_2)

    def test_target_with_name__returns_target__when_a_target_name_matches(self):
        target = self.fixture.any_target(name='MyTarget')
        xc_project = XcProject(name="MyXcProject", targets=set([target]))

        resulting_target = xc_project.target_with_name('MyTarget')

        self.assertEqual(resulting_target, target)

class XcTargetTests(TestCase):

    fixture = XcModelsFixture()

    # __init__

    def test_instantiate_xc_target(self):
        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        self.assertTrue(xc_target)
        self.assertEqual(xc_target.name, "MyXcTarget")

    def test_instantiate_xc_target__without_dependencies__has_no_dependency(self):
        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        self.assertFalse(xc_target.dependencies)
    
    def test_instantiate_xc_target__with_dependencies__has_dependencies(self):
        target_dep = self.fixture.any_target(name='MyDep')

        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST, dependencies=set([target_dep]))

        self.assertTrue(target_dep in xc_target.dependencies)
    
    def test_instantiate_xc_target__without__source_files_has_no_source_file(self):
        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        self.assertFalse(xc_target.source_files)

    def test_instantiate_xc_target__with_source_files__has_source_files(self):
        any_file = '/path/to/my/file'

        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST, source_files=set([any_file]))

        self.assertTrue(any_file in xc_target.source_files)
    
    def test_instantiate_xc_target__without__resource_files_has_no_resource_file(self):
        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        self.assertFalse(xc_target.resource_files)

    def test_instantiate_xc_target__with_resource_files__has_resource_files(self):
        any_file = '/path/to/my/file'

        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST, resource_files=set([any_file]))

        self.assertTrue(any_file in xc_target.resource_files)
    
    # __eq__

    def test_xc_targets_are_not_equal__when_different_type(self):
        xc_target_1 = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)
        xc_target_2 = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.TEST)

        self.assertFalse(xc_target_1 == xc_target_2)

    def test_xc_targets_are_not_equal__when_different_name(self):
        xc_target_1 = XcTarget(name="MyXcTarget1", target_type=XcTarget.Type.UI_TEST)
        xc_target_2 = XcTarget(name="MyXcTarget2", target_type=XcTarget.Type.UI_TEST)

        self.assertFalse(xc_target_1 == xc_target_2)
    
    def test_xc_targets_are_equal__when_same_name_and_type(self):
        xc_target_1 = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)
        xc_target_2 = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        self.assertTrue(xc_target_1 == xc_target_2)
    
    # __hash__

    def test_xc_targets_hashes_are_same__when_same_type_and_name(self):
        xc_target_1 = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)
        xc_target_2 = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        hash_1 = hash(xc_target_1)
        hash_2 = hash(xc_target_2)

        self.assertEqual(hash_1, hash_2)
    
    # __repr__

    def test_xc_target_repr_contain_name(self):
        xc_target = XcTarget(name="MyXcTarget", target_type=XcTarget.Type.UI_TEST)

        representation = str(xc_target)

        self.assertEqual(representation, "<XcTarget> MyXcTarget")